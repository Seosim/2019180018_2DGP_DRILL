from pico2d import *

open_canvas()

character = load_image("sprite.png")

def DrawImage():
    pass

def Right():
    frame = 0
    action = 0
    for x in range(50,750+1,10):
        clear_canvas()
        character.clip_draw(frame * 86+2, action*90, 86, 90, x, 90)
        update_canvas()
        frame = (frame + 1) % 10
        delay(0.05)
        get_events()

def Left():
    frame = 0
    action = 2
    for x in range(750,50-1,-10):
        clear_canvas()
        character.clip_draw(frame * 86+2, action*95, 86, 90, x, 90)
        update_canvas()
        frame = (frame + 1) % 10
        delay(0.05)
        get_events()



#Right()
Left()
