import pygame
from player import ControlKeys

# game config
WIDTH = 600
HEIGHT = 400
FPS = 60

# ball config
SPEED_BALL = 300

# player config 
PLAYER1_KEYS =  ControlKeys(pygame.K_UP, pygame.K_DOWN)
PLAYER2_KEYS = ControlKeys(pygame.K_w, pygame.K_s)
