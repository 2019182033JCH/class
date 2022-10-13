from pico2d import *
import game_framework
import logo_state
import play_state
import item_state

open_canvas()
game_framework.run(play_state)
# game_framework.run(item_state)

# delay(0)
close_canvas()
