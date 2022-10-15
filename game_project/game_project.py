from pico2d import *
import os

os.chdir('d://2019182033/class/game_project/resource')


# def handle_events():
#     global running
#     global x
#     global y
#     global x_dir
#     global y_dir
#     global last_way
#
#     events = get_events()
#     for event in events:
#         if event.type == SDL_QUIT:
#             running = False
#         elif event.type == SDL_KEYDOWN:
#             if event.key == SDLK_RIGHT:
#                 x_dir += 1
#             elif event.key == SDLK_LEFT:
#                 x_dir -= 1
#             elif event.key == SDLK_UP:
#                 y_dir += 1
#             elif event.key == SDLK_DOWN:
#                 y_dir -= 1
#             elif event.key == SDLK_ESCAPE:
#                 running = False
#         elif event.type == SDL_KEYUP:
#             if event.key == SDLK_RIGHT:
#                 last_way = 1
#                 x_dir -= 1
#             elif event.key == SDLK_LEFT:
#                 last_way = -1
#                 x_dir += 1
#             elif event.key == SDLK_UP:
#                 y_dir -= 1
#             elif event.key == SDLK_DOWN:
#                 y_dir += 1


open_canvas(1280, 720)

# background = load_image('spring_bg.png')
character = load_image('Walk.png')

# background.draw_now(640, 360)
# character.draw_now(200, 150)

running = True
x = 1280 // 2
y = 720 // 2
frame = 0
x_dir = 0
y_dir = 0
last_way = 1


x = 0
frame = 0
while x < 1280:
    clear_canvas()
    character.clip_draw(frame * 68+25, 0, 64, 64, x, 150)
    update_canvas()
    frame = (frame + 1) % 8
    x += 5
    delay(0.1)
    get_events()

# while running:
#     clear_canvas()
#     if x_dir == 0 and y_dir == 0:
#         if last_way == 1:
#             character.clip_draw(frame * 68 + 25, 100 * 3, 64, 64, x, y)
#         elif last_way == -1:
#             character.clip_draw(frame * 100, 100 * 2, 64, 64, x, y)
#     elif x_dir == 1:
#         character.clip_draw(frame * 100, 100 * 1, 64, 64, x, y)
#     elif x_dir == -1:
#         character.clip_draw(frame * 100, 100 * 0, 64, 64, x, y)
#     if y_dir == 1 or y_dir == -1:
#         if last_way == 1:
#             character.clip_draw(frame * 100, 100 * 1, 64, 64, x, y)
#         elif last_way == -1:
#             character.clip_draw(frame * 100, 100 * 0, 64, 64, x, y)
#     update_canvas()
#
#     handle_events()
#     frame = (frame + 1) % 8
#     if x_dir == 1 and x < 800:
#         x += x_dir * 5
#     elif x_dir == -1 and x > 0:
#         x += x_dir * 5
#     if y_dir == 1 and y < 600:
#         y += y_dir*5
#     elif y_dir == -1 and y > 0:
#         y += y_dir*5

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


# delay(5)

close_canvas()
