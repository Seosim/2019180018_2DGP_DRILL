import random
import time
from pico2d import *
import game_framework
import game_world

PIXEL_PER_METER = 10 / 0.3
RUN_SPEED_KPH = 50 #50km/h
RUN_SPEED_MPM = RUN_SPEED_KPH * 1000 / 60
RUN_SPEED_MPS = RUN_SPEED_MPM / 60
RUN_SPEED_PPS = RUN_SPEED_MPS * PIXEL_PER_METER

TIME_PER_ACTION = 0.3
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5

class Bird():
    def __init__(self):
        self.x, self.y = random.randint(0,1200), random.randint(300,550)
        self.frame = random.randint(0,3)
        self.action = 2
        self.dir = 1
        self.image = load_image('bird_animation.png')
        self.timer = 100

    def update(self):
        if (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) > 4: self.action -= 1
        self.action = self.action % 3


        self.frame = (self.frame + 4 * ACTION_PER_TIME * game_framework.frame_time) % 4


        if self.x + self.dir * RUN_SPEED_PPS * game_framework.frame_time == clamp(0,self.x + self.dir * RUN_SPEED_PPS * game_framework.frame_time,1200):
            self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
        else :
            self.dir *= -1


    def draw(self):
        if self.dir == 1:
            self.image.clip_composite_draw(180 * int(self.frame),165*self.action,185,170,0,'',self.x,self.y,30,30)
        else:
            self.image.clip_composite_draw(180 * int(self.frame), 165 * self.action, 185, 170, 0, 'h', self.x, self.y,
                                           30, 30)
