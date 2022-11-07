import random
from pico2d import *
import game_framework


class Bird:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.image = load_image('bird_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir
        if self.x > 800:
            self.dir = -1
        elif self.x < 0:
            self.dir = 1

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)