from pico2d import *

open_canvas()

character = load_image("sprite.png")

def DrawImage():
    pass

def Right():
    frame = 0
    action = 0
    for x in range(50,750,10):
        clear_canvas()
        character.clip_draw(frame * 86+1, 0, 86, 90, x, 300)  # x1 y1 x2 y2
        update_canvas()
        frame = (frame + 1) % 10
        delay(0.05)
        get_events()



Right()
