from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

while True:
    x = 400
    y = 90
    r = 270

    
    while x < 800:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x += 5
        delay(0.01)
    
    while y < 600:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y += 5
        delay(0.01)

    while x > 0:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x -= 5
        delay(0.01)

    while y > 90:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y -= 5
        delay(0.01)
    while x < 400:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x += 5
        delay(0.01)

    while r <= 360+ 270:
        clear_canvas_now()
        grass.draw_now(400,30)
        r += 1
        x = 400+250*math.cos(r/360*2*math.pi)
        y = 342+250*math.sin(r/360*2*math.pi)
        character.draw_now(x,y)
        delay(0.01)
        

close_canvas()
