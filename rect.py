import numpy as np

class Rect:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def move(self, x_d = 0, y_d = 0):
        self.x += x_d
        self.y += y_d

    @property
    def position(self):
        return self.x, self.y
    
    @property
    def dimention(self):
        return self.w, self.h

    @position.getter
    def position(self):
        return self.x, self.y
    
    @dimention.getter
    def dimention(self):
        return self.w, self.h

    @position.setter
    def position(self, new_position):
        self.x, self.y = new_position
    
    @dimention.setter
    def dimention(self, new_dimention):
        self.w, self.h = new_dimention
    

    def point_inside(self, x, y):
        if x > self.x and x < (self.x + self.w) and y > self.y and y < (self.y + self.h):
            return True
        else:
            return False
    
    def get_coordinates(self):
        return [[self.x, self.y], [self.x + self.w, self.y], [self.x, self.y + self.h], [self.x + self.w, self.y + self.h]]

    def collide(self, other):
        return self._collide(other) or other._collide(self)

    def _collide(self, other):
        return np.any(list(map(lambda point: self.point_inside(*point) , other.get_coordinates())))