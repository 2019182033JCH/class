from pico2d import *
import logo_state
# import play_state

start_state = logo_state

open_canvas()
start_state.enter()
# game main loop code
while start_state.running:
    start_state.handle_events()
    start_state.update()
    start_state.draw()
    delay(0.05)

start_state.exit()
# finalization code
close_canvas()

