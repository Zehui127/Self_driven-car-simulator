This is the timeline that the project should follow.  
The headings provide the version number and the date that it should be completed by.  
Each version has a set description of the features that must be implemented in that version.

# v0.1 - 23/11/17

### Simulator proof of concept
- Pygame embedded into GTK window
- Drawing lanes
- Drawing car
- User input
- Lane switching controlled by user

# v0.2 - 14/12/17

### Simulator
- Other vehicles spawning (with lower speed than user, start after a few seconds)
- Ability to check for collisions between user car and other vehicles
- Better visuals
  - Sprites for vehicles
  - Draw road markings to visually divide lanes (that don't move)

### AUDRI proof of concept
- Using the Tensorflow library

- Training data
  - Can read sets of stored data
  - One element of set indicates action (left, stay, right)
  - Other elements - lane, distance to closest vehicle, closest vehicle's speed, lane of closest
vehicle

- Train reward function using provided data

- Scripts - utilities used for testing
  - Generate random training data

# v0.3 - 5/1/18

### Simulator
- GUI panel (on right)
  - Current lane
  - Current speed (km/h)
  - Mode (user/AUDRI)
  - Distance travelled
  - Session duration
  - Collision counter

- Visualiser
  - Able to receive commands from AUDRI
    - Change lane left or right

### AUDRI
- Train policy using training data
- Output decision using policy

 AUDRI items for this deadline are incomplete. Please see below;
 
# v0.31 - 1/2/18

### AUDRI
 - Have initial code in place for the AUDRI NN
 - Code in place to allow AUDRI to control the vehicle

# v0.4 - 8/2/18

### GUI
- Initial window giving the options of driving, training, and testing AUDRI

### Simulator
- Prompt to choose file name to store training data in - default to (d:m:y h:m:s)
- Ability to pause (automatic when starting, using a key)
- Pause button in GUI

- Better visuals
  - Improve sprites (if necessary)
  - 'Grass' in the offroad lanes
  - Road markings move as the user car moves

### AUDRI
- GUI to load training data and train reward function
- GUI to start simulator in AUDRI mode to train policy 

The above objectives for AUDRI have been extended, please view below for the new objectives for this deadline;

 - AUDRI is able to interact with simulator
 - AUDRI is able to record training data 

# v0.41 - 22/2/18  
### AUDRI
- GUI to load training data and train reward function
- GUI to start simulator in AUDRI mode to train policy

# v1.0 - 1/3/18
The first 'releasable' version.  
The project should provide the bare minimum functionality that would allow for it to be
demonstrated and used by any person.

# Stretch features
Potential features that could be implemented to improve or extend the functionality of the project

### Simulator
- Training data
  - Extend training data through multiple drives

- Tutorial
  - Information on how to use the system (link to the project page?)
  - Show controls to user (hotkey + icon - popup in the visualiser)

- Configuration
  - Can be loaded from/saved in files (also along with training data?)
  - Random seed (to achieve consistent spawning of vehicles)
  - Speed of vehicles (possible ranges, if randomised)
  - Speed of user car
  - Acceleration of other vehicles (randomised)
  - Whether car can drive offroad
  - Default file names for training data and models

- AUDRI
  - Export model into file - can save and restore it
