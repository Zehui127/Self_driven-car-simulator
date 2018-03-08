'''The visualiser of the simulator - the game the user plays
Uses the PyGame library
'''
import os, platform
from threading import Thread
from enum import Enum
from time import time
from random import randint

import pygame

from .vehicles import Obstacle, Car
###################################
import numpy as np
import random
import csv
from .nn import neural_net, LossHistory
import os.path
import timeit
GAMMA = 0.9#TODO delete
savedModelAddress = 'saved-models/128-128-64-50000-50000.h5'
loadedModel = neural_net(5, [128, 128], savedModelAddress)

######################################
class Actions(Enum):
    '''Enumerations of the actions that the simulator can receive'''
    LEFT = 0 # move to left lane
    RIGHT = 1 # move to right lane

# Key names that map on to actions. Keys are key names, values actions
# Key names are found in gdk/gdkkeysyms.h, without prefix GDK_KEY_
# https://git.gnome.org/browse/gtk+/tree/gdk/gdkkeysyms.h#n39
KEYS = {
    'Left': Actions.LEFT,
    'Right': Actions.RIGHT,
}

class SimulatorVisualiser():
    '''The visualiser of the simulator'''
    _fps = 0 # internal FPS target
    _shutdown = False # whether the current class is shutting down
    _targetDrawDelay = 0 # delay in between draws to achieve FPS
    _lastSpawn = 0 # last timestamp an obstacle vehicle was spawned
    _lastPlay = 0
    _obstacles = [] # list of current obstacle vehicles

    '''Handles the visualisation of the simulator'''
    def __init__(self, config, windowID):
        '''Initialise configuration and Pygame
        :param config: :class:`SimulatorConfig`
        :param windowID: :class:`str` set as the SDL_WINDOWID environment
        variable'''

        if windowID:
            os.putenv('SDL_WINDOWID', windowID)

            if platform.system == 'Windows':
                os.environ['SDL_VIDEODRIVER'] = 'windib'

        pygame.init()
        pygame.display.set_mode(config.VisualiserSize, 0, 0)

        self._config = config
        self._lastTick = time()

        self.fps = config.FPS
        self.canvas = pygame.display.get_surface()
        self.car = Car(config, self) # car that is controlled by user
        self.collisions = 0

        self.drawThread = Thread(name='draw', target=self.draw)
        self.drawThread.start()
        self.trainer = Trainer()

    def shutdown(self):
        '''Handle visualiser shutdown'''
        self._shutdown = True
        self.drawThread.join(timeout=1/100)

    @property
    def fps(self):
        '''Return the current set FPS'''
        return self._fps

    @fps.setter
    def fps(self, val):
        '''Set the target draw delay, store desired FPS'''
        self._fps = val
        self._targetDrawDelay = (int)(1/val *1000)

    def tick(self):
        '''This method tries to run in intervals of 1ms
        Must return True to continue running
        Use to perform update logic using time since the previous tick
        '''
        now = time()

        # delta time - time in seconds since last tick
        dt = now -self._lastTick
        self._lastTick = now

        # call tick on vehicles, keep only ones on screen
        self.car.tick(dt)
        self._obstacles = [ob for ob in self._obstacles if ob.tick(dt)]

        # spawn obstacles
        if now -self._lastSpawn >= self._config.ObstacleInterval:
            ob = Obstacle(self._config, self)
            ob.lane = randint(
                1 if self._config.OffroadAllowed else 0,
                self._config.Lanes -(0 if self._config.OffroadAllowed else 0))
            self._obstacles.append(ob)
            self._lastSpawn = now
            #status, reward = self.statusVector()
            #self.play(status)
        # check for collisions
        self.collisions += sum(ob.hasCollided for ob in self._obstacles)
        '''
        status, reward = self.statusVector()
        self.trainer.train(status,self)
        '''
        
        if now -self._lastPlay >= 0.5:
            status, reward = self.statusVector()
            self.play(status)
            self._lastPlay = now
        
        #status, reward = self.statusVector()
        #self.trainer.train(status,self)
        #self.play(status)
        '''trainer.train(status,self)
            


        '''
        return True

    def keyPress(self, key):
        '''Handle key presses and perform the actions they map onto'''
        if key not in KEYS:
            return

        act = KEYS[key]
        if act == Actions.LEFT:
            self.car.lane -= 1

        elif act == Actions.RIGHT:
            self.car.lane += 1

    def draw(self):
        '''Updates the canvas
        Attempts to achieve target FPS by blocking
        As such, it should run in its own thread so other things can be done in
        the background
        Should run in and endless loop to continuously redraw
        Should exit if self._shutdown is True
        '''
        while not self._shutdown:
            size = self._config.VisualiserSize
            # draw a background
            pygame.draw.rect(
                self.canvas, self._config.OffroadColor,
                pygame.Rect(0, 0, size[0], size[1]))

            self.drawLanes()

            # draw obstacle vehicles
            for ob in self._obstacles:
                ob.draw(self.canvas)

            self.car.draw(self.canvas) # draw user car

            pygame.display.flip()
            pygame.time.wait(self._targetDrawDelay)

    def drawLanes(self):
        '''Draw all road lanes'''
        pygame.draw.rect(
            self.canvas, self._config.LaneColor,
            pygame.Rect(
                self._config.OffroadWidth, 0,
                self._config.OffroadWidth *self._config.Lanes,
                self._config.VisualiserSize[1]))
    #TODO find out the coordinate system of the car
    def statusVector(self):
        '''Return the status vector, and reward function
        The status vector is list of 5 elements
        The reward function is designed so that the optimal performence is to avoid collision and stay within the lane'''
        minObst = self.closestObst()
        curLane =  int(self.car._lane)
        distanceLane1 = minObst[0]
        distanceLane2 = minObst[1]
        distanceLane3 = minObst[2]
        distanceCurrent = minObst[curLane-1] if (curLane in range(1,3)) else 1000
        #minOsbt(curLane)
        if not(curLane == 0 or curLane== 4):
            distanceCurrent =  minObst[curLane-1]#the distance to the single cloest car at cuurent lane
        #TODO change fixed number of lanes
        crash = -500 if distanceCurrent<50 and distanceCurrent>=0 else 0
        reward = (-100 if (curLane==0 or curLane== self._config.Lanes+1) else 0) + crash # -10 punishment for offlane, -20 punishment for collision
        return np.array([[curLane,distanceCurrent,distanceLane1,distanceLane2,distanceLane3]]),reward
    def closestObst(self):
        '''return the y position of closest car on each lane, assume allow offlane'''
        minObst=[1000]*self._config.Lanes
        for ob in self._obstacles:
            lane = ob._lane
            pos = self.car._pos[1]-ob._pos[1] 
            if pos<minObst[lane-1] and pos>=0:
                minObst[lane-1]=pos
        return minObst#minObst[1]
    def applyAction(self,action):
        if action==0:
            self.car.lane -= 1
        elif action == 1:
            self.car.lane+=1
        elif action == 2:#TODO change the number to 
            self.car.lane = 0
        elif action == 3:
            self.car.lane = 4
    def play(self,state):
        action = (np.argmax(loadedModel.predict(state, batch_size=1)))
        print(action)
        self.applyAction(action)

####################################################################
class Trainer:
    '''Class to train the model'''
    def __init__(self,params= {"batchSize": 64,"buffer": 50000, "nn": [128,128] }):
        self._filename = str(params['nn'][0]) + '-' + str(params['nn'][1]) + '-' + \
                str(params['batchSize']) + '-' + str(params['buffer'])
        self.observe = 1000  # Number of frames to observe before training.
        self.epsilon = 1
        self.train_frames = 100000  # Number of frames to play.
        self.batchSize = params['batchSize']
        self.buffer = params['buffer']
        self.t = 0 #number of iteration
        self.replay = []  # stores tuples of (S, A, R, S').
        self.loss_log = []
        self.model = neural_net(5, [128,128])
    def train(self,state,simulator):
        print(self.t)
        self.t+=1
        if random.random()<self.epsilon or self.t<self.observe:
            action = np.random.randint(0, 4)
        else:
            # Get Q values for each action.
            qval = self.model.predict(state, batch_size=1)
            print(qval)#21
            action = (np.argmax(qval)) 
        # Take action, observe new state and get our treat.
        simulator.applyAction(action)
        new_state,reward = simulator.statusVector()
        # Experience replay storage.
        self.replay.append((state, action, reward, new_state))
        if self.t > self.observe:
            # If we've stored enough in our buffer, pop the oldest.
            if len(self.replay) > self.buffer:
                self.replay.pop(0)
            # Randomly sample our experience replay memory
            minibatch = random.sample(self.replay, self.batchSize)
            # Get training values.
            X_train, y_train = self.process_minibatch2(minibatch, self.model)
            # Train the model on this batch.
            history = LossHistory()
            self.model.fit(
                X_train, y_train, batch_size=self.batchSize,
                nb_epoch=1, verbose=0, callbacks=[history]
            )
                    # Decrement epsilon over time.
        if self.epsilon > 0.1 and self.t > self.observe:
            self.epsilon -= (1.0/self.train_frames)

        if self.t % 25000 == 0:
            self.model.save_weights('saved-models/' + self._filename + '-' +
                               str(self.t) + '.h5',
                               overwrite=True)
            print("Saving model %s - %d" % (self._filename, self.t))
        '''TODO need to change to class functions'''
    def process_minibatch2(self,minibatch, model):
        # by Microos, improve this batch processing function 
        #   and gain 50~60x faster speed (tested on GTX 1080)
        #   significantly increase the training FPS
        
        # instead of feeding data to the model one by one, 
        #   feed the whole batch is much more efficient

        mb_len = len(minibatch)

        old_states = np.zeros(shape=(mb_len, 5)) #TODO Notice number of features 
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
        non_term_inds = np.where(rewards != -500)[0]   #TODO
        term_inds = np.where(rewards == -500)[0]

        y[non_term_inds, actions[non_term_inds].astype(int)] = rewards[non_term_inds] + (GAMMA * maxQs[non_term_inds])#if not -500 then using current one
        y[term_inds, actions[term_inds].astype(int)] = rewards[term_inds]

        X_train = old_states
        y_train = y
        return X_train, y_train