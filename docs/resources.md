### Introduction
This file contains useful resources for the development of this project

### Libraries
[Tkinter documentation](https://wiki.python.org/moin/TkInter)  
Tkinter is the cross-platform GUI library for Python.  
It's used for the project GUI. 

[Pygame documentation](https://www.pygame.org/docs)  
Pygame is a 2D Python game library.
It powers the visualiser ('game') of the simulator.
A Pygame screen is embedded into the GTK window.

[Tensorflow documentation](https://www.tensorflow.org/api_docs/python/)  
Tensorflow is an open-source software library for Machine Intelligence.
It will primarily used for the training of the automated system using inverse 
reinforcement learning.

### Coding Examples For AUDRI 
This section provides coding examples that may be useful for the AUDRI side of
the project. It consists of two other repositories.

[Apprenticeship learning using Inverse Reinforcement Learning](https://jangirrishabh.github.io/2016/07/09/virtual-car-IRL/)
This is an in-depth description of another project which uses IRL to train a
car to move around a track using sensors to detect obstructions.  
It is worth noting that this project may be using an older version of Python
and DOES NOT list all of the dependencies. These can be found in another 
repository, using a different algorithm, which this one is based on.  
If you want to take a look at this [here](https://github.com/harvitronix/reinforcement-learning-car).

[Toy Car IRL](https://github.com/jangirrishabh/toyCarIRL)
This is the repository for the above project, containing all their code.

EDIT: These resources for AUDRI are probably too complex, but may still be useful as we adapt our code. 

### AUDRI FYI - useful info for coding AUDRI
Agent – The Agent is essentially our car, with the AUDRI code. 

Sensors – We will have a sensor to detect how close the car in front of us is. This may be expanded so that there is a sensor in all lanes for our agent. (so it will know which lane is clear)

State Space – We will have 4 observable features. Normalisation is done on the three sensors;


 - Distance Sensor Lane 1 (distance to obstacle divided by total vertical pixels of the screen)
 
 - Distance Sensor Lane 2 (distance to obstacle divided by total vertical pixels of the screen)
 
 - Distance Sensor Lane 3 (distance to obstacle divided by total vertical pixels of the screen)
 
 - Boolean to indicate a crash/collision with other vehicles. This is indicated by state "Done", which is a boolean indicating when a crash has occured and the simulation should end. 


Rewards – The reward can be taken by timing the expert from the start of the simulation, until a collision occurs. 

Available Actions – The available actions are to more left, right, or stay in place however these actions can alter depending on the lane, for example if the agent is in the far right lane or hard shoulder, it will not be able to move into a next lane. 

Obstacles – The environment consists of three lanes, in which cars can spawn at random at given time intervals. The number of collisions are recorded in the training data, and the simulation only ends when the user ends the session. 

Agent State - The starting position is the same for all sessions
