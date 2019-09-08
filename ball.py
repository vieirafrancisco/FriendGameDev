import pygame
from config import *
from rect import Rect
import random

class Ball:
    def __init__(self,radius, fps, speed, posx, posy):
        self.radius = radius
        self.color = (255,255,255)
        self.speedx = speed
        self.speedy = speed
        self.fps = fps
        self.rect = Rect(posx-radius, posy-radius, 2*radius, 2*radius)


    def move(self):

        posx, posy = self.rect.position

        if posy >= HEIGHT or posy < 0:
            self.speedy = -(self.speedy)

        self.rect.move(self.speedx / self.fps, self.speedy / self.fps)

    def collision(self, player_rect):
        posx, posy = self.rect.position

        if self.rect.collide(player_rect):
            if posx < WIDTH/2:
                self.speedx = abs(self.speedx)
            elif posx > WIDTH/2:
                self.speedx = -abs(self.speedx)

    def draw(self, surface):
        posx, posy = self.rect.position
        posx = posx + self.radius
        posy = posy + self.radius
        pygame.draw.circle(surface, self.color, (int(posx), int(posy)), self.radius)
    

    def update(self):
        self.move()

    def reset_pos(self):
        self.rect.position = [int(WIDTH/2), int(HEIGHT/2)]
        self.speedx = self.speedx * random.choice([-1,1])
        self.speedy = self.speedy * random.choice([-1,1])

    def out_off_screen(self):
        posx, posy = self.rect.position

        if posx < 0:
            self.reset_pos()
            return -1
        if posx > WIDTH:
            self.reset_pos()
            return 1 
        return 0     
