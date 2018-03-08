'''Utility functions and classes'''
import os
import pygame

def loadSprite(path, scale=1):
    '''Load an image relative to the sprites/ directory as a pygame image
    scale if desired'''

    src = os.path.join(os.path.dirname(__file__) +'/../sprites', path)

    if scale == 1:
        return pygame.image.load(src)

    img = pygame.image.load(src).convert_alpha()
    size = img.get_size()
    return pygame.transform.scale(
        img, tuple(map(lambda x: int(x *scale), size)))
