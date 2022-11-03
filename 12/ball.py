from pico2d import *

import game_world


#import game_world

class Ball:
    image = None

    def __init__(self, x = 300, y = 50,velocity = 1):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y, self.velocity = x, y, velocity

    def draw(self):
        self.image.draw(self.x,self.y)

    def update(self):
        self.x += self.velocity
        if self.x != clamp(50,self.x,750):
            game_world.remove_object(self)