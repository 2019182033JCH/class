from pico2d import *
import os

os.chdir('d://2019182033/class/game_project/resource')


def handle_events():
    global running
    global x
    global y
    global x_dir
    global y_dir
    global last_way

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                x_dir += 1
            elif event.key == SDLK_LEFT:
                x_dir -= 1
            elif event.key == SDLK_UP:
                y_dir += 1
            elif event.key == SDLK_DOWN:
                y_dir -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                last_way = 1
                x_dir -= 1
            elif event.key == SDLK_LEFT:
                last_way = -1
                x_dir += 1
            elif event.key == SDLK_UP:
                y_dir -= 1
            elif event.key == SDLK_DOWN:
                y_dir += 1


open_canvas()

background = load_image('summer_bg.png')
# character = load_image('animation.png')

# background.draw_now(640, 360)
# character.draw_now(200, 150)

running = True
x = 200
y = 150
frame = 0
x_dir = 0
y_dir = 0
last_way = 1


# x = 0
# frame = 0
# while x < 1280:
#     clear_canvas()
#     character.clip_draw(frame * 67+30, 0, 64, 64, x, 150)
#     update_canvas()
#     frame = (frame + 1) % 8
#     x += 5
#     delay(0.1)
#     get_events()

while running:
    clear_canvas()
    # background.draw_now(400, 300)

    if x_dir == 0 and y_dir == 0:
        if last_way == 1:
            character = load_image('idle.png')
            frame = (frame + 1) % 4
            delay(0.1)
            character.clip_draw(frame * 67, 0, 75, 100, x, y)
        elif last_way == -1:
            character = load_image('idler.png')
            frame = (frame + 1) % 4
            delay(0.1)
            character.clip_draw(frame * 67, 0, 75, 100, x, y)
    elif x_dir == 1:
        character = load_image('Walk.png')
        frame = (frame + 1) % 8
        delay(0.01)
        character.clip_draw(frame * 67 + 30, 0, 64, 100, x, y)
    elif x_dir == -1:
        character = load_image('Walker.png')
        frame = (frame + 1) % 8
        delay(0.01)
        character.clip_draw(frame * 67 + 20, 0, 64, 100, x, y)
    if y_dir == 1 or y_dir == -1:
        if last_way == 1:
            character = load_image('Walk.png')
            frame = (frame + 1) % 8
            delay(0.01)
            character.clip_draw(frame * 67 + 30, 0, 64, 100, x, y)
        elif last_way == -1:
            character = load_image('Walker.png')
            frame = (frame + 1) % 8
            delay(0.01)
            character.clip_draw(frame * 67 + 20, 0, 64, 100, x, y)
    update_canvas()

    handle_events()
    if x_dir == 1 and x < 800:
        x += x_dir * 10
    elif x_dir == -1 and x > 0:
        x += x_dir * 10
    if y_dir == 1 and y < 600:
        y += y_dir * 10
    elif y_dir == -1 and y > 0:
        y += y_dir * 10

    delay(0.05)

close_canvas()
