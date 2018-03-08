# Training Data Specifications
## Layout
Following Row/Column layout

Column specifies current states/available actions/outcomes

- State (crashed/driving)
- Action (move left/move right)
- Position (Left/middle/right
- Distance Ahead (in meters)
- Space to left/right (in meters)

Row specifies current state of vehicle at each simulation frame
- For example, in frame 10, the location might be MIDDLE, with possible actions being to move left or right and if the car crashed during that frame.  This data stored on one row.
- All data stored in integer format, for example; State CRASHED = 2, State DRIVING = 0, Action LEFT = 1

## Storage

- Saved as CVS file 
- File location accessible by AUDRI
- Generating Data
- Manual creating document (Data typed into file manually (for testing))
- Randomly generated data (Possibility to use another algorithm which takes random actions)
- Expert generated data (Able to record expert drivers actions in each frame)

## Possible Additional Specifications
- Additional Positions (Off Road, new lanes)
- Additional Actions (Speed up/Slowdown)
(Additional data “Speed” specified in mph.)
- File storage may alter during development
- Additional data sets may be added during development 
- States/actions/positions may alter with changing requirements/specifications
