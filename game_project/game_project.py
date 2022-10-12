from pico2d import *
import os

os.chdir('d://2019182033/class/game_project/resource')

open_canvas(1280, 720)

background = load_image('spring_bg.png')
character = load_image('Protect.png')

background.draw_now(640, 360)
character.draw_now(200,150)
# class background:
#     def __init__(self):
#         self.image = load_image('spring_bg.png')
#
#     def draw(self):
#         self.image.draw(640, 360)
#
#
# class Boy:
#     def __init__(self):
#         self.x, self.y = 0, 90
#         self.frame = 0
#         self.image = load_image('Protect.png')
#
#     def draw(self):
#         self.image.clip_draw(200, 100)


delay(5)

close_canvas()
