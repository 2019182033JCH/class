import pico2d
import play_state
import logo_state
pico2d.open_canvas()
# start_state = logo_state  # 모듈을 변수로 설정
#

# start_state.enter()  # 초기화
# # 게임 루프
# while start_state.running:
#     start_state.handle_events()
#     start_state.update()
#     start_state.draw()
#     pico2d.delay(0.01)
# start_state.exit()  # 종료
#
# start_state = play_state
# start_state.enter()  # 초기화
# # 게임 루프
# while start_state.running:
#     start_state.handle_events()
#     start_state.update()
#     start_state.draw()
#     pico2d.delay(0.01)
# start_state.exit()  # 종료


states = [logo_state, play_state]
for state in states:
    state.enter()
    while state.running:
        state.handle_events()
        state.update()
        state.draw()
    state.exit()

pico2d.close_canvas()

