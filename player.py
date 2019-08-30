import pygame
from rect import Rect

class ControlKeys():
    def __init__(self, up_key_code, down_key_code, left_key_code = None, right_key_code = None):
        self.up_key_code = up_key_code
        self.down_key_code = down_key_code
        self.left_key_code = left_key_code
        self.right_key_code = right_key_code

class Player:
    def __init__(self, posx, posy, speed, fps, control_keys,width = 5, height = 60):
        self.fps = fps
        self.control_keys = control_keys
        self.score = 0
        self.speed = speed
        self.rect = Rect(posx, posy, width, height)
    
    def move(self, pressed_keys):
        if pressed_keys[self.control_keys.up_key_code]:
            self.rect.move(y_d = -self.speed / self.fps)
        elif pressed_keys[self.control_keys.down_key_code]:
            self.rect.move(y_d = self.speed / self.fps)
        elif self.control_keys.left_key_code != None and pressed_keys[self.control_keys.left_key_code]:
            self.rect.move(x_d = -self.speed / self.fps)
        elif self.control_keys.right_key_code != None and pressed_keys[self.control_keys.right_key_code]:
            self.rect.move(x_d = self.speed / self.fps)


    def draw(self, surface):
        pygame.draw.rect(surface, (255,255,255), (*self.rect.position, *self.rect.dimention))
    
    def update(self, pressed_keys):
        self.move(pressed_keys)


