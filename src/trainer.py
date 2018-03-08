import numpy as np
import random
import csv
from nn import neural_net, LossHistory
import os.path
import timeit

from visualiser import SimulatorVisualiser
from config import SimulatorConfig

class Trainer:
	'''Class to train the model'''
	def __init__(self,params= {"batchSize": 64,"buffer": 50000, "nn": [128,128] }):
		self._filename = str(params['nn'][0]) + '-' + str(params['nn'][1]) + '-' + \
				str(params['batchSize']) + '-' + str(params['buffer'])
		self.observe = 1000  # Number of frames to observe before training.
		self.epsilon = 1
		self.train_frames = 100000  # Number of frames to play.
		self.batchSize = params['batchSize']
		buffer = params['buffer']
		self.t = 0 #number of iteration
		self.replay = []  # stores tuples of (S, A, R, S').
		self.loss_log = []
		self.model = neural_net(5, [128,128])
	def train(self,state,simulator):
		self.t+=1
		if random.random()<self.epsilon or self.t<self.observe:
			action = np.random.randint(0, 4)
		else:
			# Get Q values for each action.
			qval = self.model.predict(state, batch_size=1)
			action = (np.argmax(qval)) 
		# Take action, observe new state and get our treat.
		simulator.applyAction(action)
		reward, new_state = simulator.statusVector()
		# Experience replay storage.
		self.replay.append((state, action, reward, new_state))
		if t > observe:
			# If we've stored enough in our buffer, pop the oldest.
			if len(self.replay) > buffer:
				self.replay.pop(0)
			# Randomly sample our experience replay memory
			minibatch = random.sample(self.replay, self.batchSize)
			# Get training values.
			X_train, y_train = process_minibatch2(minibatch, self.model)
			# Train the model on this batch.
			history = LossHistory()
			model.fit(
				X_train, y_train, batch_size=batchSize,
				nb_epoch=1, verbose=0, callbacks=[history]
			)
					# Decrement epsilon over time.
		if self.epsilon > 0.1 and self.t > self.observe:
			self.epsilon -= (1.0/train_frames)

		if self.t % 25000 == 0:
			self.model.save_weights('saved-models/' + self._filename + '-' +
							   str(self.t) + '.h5',
							   overwrite=True)
			print("Saving model %s - %d" % (self._filename, self.t))
		'''TODO need to change to class functions'''
		def process_minibatch2(minibatch, model):
			# by Microos, improve this batch processing function 
			#   and gain 50~60x faster speed (tested on GTX 1080)
			#   significantly increase the training FPS
			
			# instead of feeding data to the model one by one, 
			#   feed the whole batch is much more efficient

			mb_len = len(minibatch)

			old_states = np.zeros(shape=(mb_len, 5))
			actions = np.zeros(shape=(mb_len,))
			rewards = np.zeros(shape=(mb_len,))
			new_states = np.zeros(shape=(mb_len, 5))

			for i, m in enumerate(minibatch):
				old_state_m, action_m, reward_m, new_state_m = m
				old_states[i, :] = old_state_m[...]
				actions[i] = action_m
				rewards[i] = reward_m
				new_states[i, :] = new_state_m[...]

			old_qvals = model.predict(old_states, batch_size=mb_len)
			new_qvals = model.predict(new_states, batch_size=mb_len)

			maxQs = np.max(new_qvals, axis=1)
			y = old_qvals
			non_term_inds = np.where(rewards != -500)[0]
			term_inds = np.where(rewards == -500)[0]

			y[non_term_inds, actions[non_term_inds].astype(int)] = rewards[non_term_inds] + (GAMMA * maxQs[non_term_inds])
			y[term_inds, actions[term_inds].astype(int)] = rewards[term_inds]

			X_train = old_states
			y_train = y
			return X_train, y_train