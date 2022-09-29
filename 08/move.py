from pico2d import *

width = 1280
height = 720

def out():
    global x,y

    if x < 50: x = 0+50
    if x > width-50: x = width-50
    if y < 50: y = 0+50
    if y > height-50: y = height-50

def handle_events():
    global running

    global action
    global dir

    global pushR
    global pushL
    global pushU
    global pushD

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir = 1
                action = 1
                pushR = True
            elif event.key == SDLK_LEFT:
                dir = 0
                action = 0
                pushL = True
            elif event.key == SDLK_UP:
                pushU = True
            elif event.key == SDLK_DOWN:
                pushD = True
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                action = 3
                pushR = False
            elif event.key == SDLK_LEFT:
                action = 2
                pushL = False
            elif event.key == SDLK_UP:
                action = dir+2
                pushU = False
            elif event.key == SDLK_DOWN:
                action = dir+2
                pushD = False



open_canvas(width,height)
background = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x = 1280 // 2
y = 60
frame = 0
action = 3
dir = 1

pushR = False
pushL = False
pushU = False
pushD = False

while running:
    clear_canvas()
    background.draw(width//2, height//2)
    character.clip_draw(int(frame) * 100, 100 * action, 100, 100, x, y)
    update_canvas()

    handle_events()
    frame = (frame + 0.25) % 8

    if pushR:
        x+= 4
        action = 1
    if pushL:
        x-= 4
        action = 0
    if pushU:
        action = dir
        y += 4
    if pushD:
        action = dir
        y -= 4
    out()
    delay(0.01)

close_canvas()

