from pico2d import *

open_canvas()

character = load_image("sprite.png")

def DrawImage(x,y,fr,ac):
    clear_canvas()
    character.clip_draw(fr * 86 + 2, ac * 95, 86, 90, x, y)
    update_canvas()
    fr = (fr+1)%10
    delay(0.05)
    get_events()

def Right():
    frame = 0
    action = 0
    for x in range(50,750+1,10):
        DrawImage(x,90,frame,0)
        frame = (frame+1)%10

def Left():
    frame = 0
    action = 2
    for x in range(750,50-1,-10):
        DrawImage(x,90,frame,2)
        frame = (frame+1)%10



Right()
Left()
