'''Vehicle classes used by the game'''
from .util import loadSprite

class Vehicle:
    '''A vehicle in the game'''

    def __init__(self, config, game):
        '''Sets the parent game instance
        :param config: :class:`SimulatorConfig`'''
        self._config = config
        self._color = config.VehicleColor

        # real 2D velocity vector, applied each tick
        self._velocity = (
            0, -(config.ObstacleSpeed -config.CarSpeed) *config.PixelMetreRatio)

        self._game = game
        self._speed = 0 # virtual speed (eg km/h)
        self._pos = (0, 0) # real 2D position tuple (x,y)
        self._lane = 0
        self._spriteScale = 1
        self._sprite = 'obstacle.png'
        self._image = None
        self._rect = None

    @property
    def sprite(self):
        '''Return or create sprite object with the given _sprite attribute
        Resizes by multiplying by _spriteScale'''
        if not self._image is None:
            return self._image

        self._image = loadSprite(self._sprite, self._spriteScale)
        return self._image

    def draw(self, canvas):
        '''Draw the vehicle'''
        #pygame.draw.rect(canvas, self._color, self._rect)
        canvas.blit(self.sprite, self._rect)

    @property
    def lane(self):
        '''Get current lane of vehicle'''
        return self._lane

    @lane.setter
    def lane(self, val):
        '''Set the lane number of the vehicle
        Vehicle is centered in its lane
        The lane values are restricted to the lanes available'''

        if val < 0 or val > self._config.Lanes -1 \
            +(2 if self._config.OffroadAllowed else 0):
            return

        self._lane = val

        if val < 1 and self._config.OffroadAllowed:
            self._rect.centerx = self._config.OffroadWidth /2
            return

        # add offroad offset if needed
        self._rect.centerx = self._config.OffroadWidth

        self._rect.centerx += (val + \
            (-0.5 if self._config.OffroadAllowed else 0.5)) \
            *self._config.LaneWidth

    @property
    def speed(self):
        '''Get the vehicle speed in km/h'''
        return self._speed

    @speed.setter
    def speed(self, val):
        '''Set the vehicle speed in km/h
        Also sets the real velocity vector, relative to user car'''
        self._speed = val
        # set velocity relative to driver
        # TODO neater implementation of vector arithmetic
        self._velocity = tuple(
            self._velocity[0],
            self._config.CarSpeed -val)

class Obstacle(Vehicle):
    '''Obstacle vehicles that the user has to avoid'''

    def __init__(self, config, game):
        super(Obstacle, self).__init__(config, game)
        self._spriteScale = config.ObstacleScale
        self._rect = self.sprite.get_rect()
        self._collided = False
        self._pos = (
            0, -self._rect.size[1])
        self._rect.y = self._pos[1]

        self.lane = 0

    def tick(self, dt):
        '''Called regularly to perform update logic.
        Return False to indicate vehicle is entirely off screen and should be
        removed'''
        self._pos = (
            0, self._pos[1] +self._velocity[1] *dt)
        self._rect.y = self._pos[1]

        return self._game.canvas.get_rect().colliderect(self._rect)

    @property
    def hasCollided(self):
        '''Returns whether the vehicle has started colliding this tick
        Updates Vehicle._collided'''
        collision = self._game.car._rect.colliderect(self._rect)
        ret = collision and not self._collided
        self._collided = collision or self._collided
        return ret

class Car(Vehicle):
    '''The user-controlled car'''

    def __init__(self, config, game):
        super(Car, self).__init__(config, game)
        self._color = config.CarColor
        self._spriteScale = config.CarScale
        self._sprite = 'car.png'
        self._rect = self.sprite.get_rect()

        self._pos = (0,config.VisualiserSize[1] -self._rect.size[1] -25)
        self._rect.y = self._pos[1]

        self.lane = (self._config.Lanes -1) /2 \
            +(1 if self._config.OffroadAllowed else 0)

    def tick(self, dt):
        '''Car tick method, currently does nothing'''
        pass
