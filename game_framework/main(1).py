from pico2d import *
# import play_state
import logo_state
start_state = logo_state  # 모듈을 변수로 저장

open_canvas()
start_state.enter()  # 초기화

# game main loop code
while start_state.running:
    start_state.handle_events()
    start_state.update()
    start_state.draw()
    delay(0.05)
exit()  # 종료
close_canvas()
