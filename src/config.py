'''Configuration classes for all of the components'''

# Example used from https://stackoverflow.com/questions/6760685
class Singleton(type):
    '''Metaclass that allows for singleton behaviour'''
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls) \
                .__call__(*args, **kwargs)
        return cls._instances[cls]

class SimulatorConfig(metaclass=Singleton):
    '''Stores configuration related to the simulator'''
    # GUI

    # Width of the GUI on the side of the window
    GUIWidth = 176

    # Related to Pygame

    # Target milliseconds between each simulation tick
    TickRate = 5
    # Dimensions of the game canvas
    VisualiserSize = (500, 600)
    # target frames per second to be drawn
    FPS = 60

    # Appearance

    LaneWidth = 100
    LaneColor = (63, 63, 63)
    OffroadColor = (26, 175, 0)
    CarColor = (0, 200, 0)
    VehicleColor = (200, 0, 0)
    CarScale = 0.35
    ObstacleScale = 0.5

    # Ratio of pixels to metres, useful for visualising speeds (float)
    PixelMetreRatio = 50

    # Functionality

    # Number of lanes to use (int)
    Lanes = 3
    # Speed of main car in (m/s)
    CarSpeed = 10
    # Speed of obstacle vehicles (m/s)
    ObstacleSpeed = 8
    # Interval between spawing obstacles (secs)
    ObstacleInterval = 2

    # Whether the car can go offroad
    OffroadAllowed = True

    def __init__(self):
        '''Calculate properties'''
        self.OffroadWidth = \
            (self.VisualiserSize[0] -self.Lanes *self.LaneWidth) /2
