import random

import game_framework
from pico2d import *

import game_world
import server

import background

class Ball:
    image = None
    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('./ball21x21.png')

        self.x = random.randint(100, server.background.w - 100)
        self.y = random.randint(100, server.background.h - 100)

    def handle_collision(self,other, group):
        if group == 'BOY : BALL':
            game_world.remove_object(self)

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def update(self): pass

    def draw(self):
        sx, sy = self.x - server.background.window_left, self.y - server.background.window_bottom
        self.image.draw(sx,sy)


