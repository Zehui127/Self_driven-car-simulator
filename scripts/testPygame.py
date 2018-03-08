'''A short script to test that Pygame is installed and can run correctly'''
import pygame

pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
display.fill((255, 0, 0))

pygame.display.flip()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
