from pico2d import *

#이벤트 정의
RD,LD,RU,LU,TIMER,AD,AU = range(7)

key_event_table = {
    (SDL_KEYDOWN,SDLK_RIGHT) : RD,
    (SDL_KEYDOWN,SDLK_LEFT) : LD,
    (SDL_KEYUP,SDLK_RIGHT) : RU,
    (SDL_KEYUP, SDLK_LEFT): LU,
    (SDL_KEYDOWN, SDLK_a): AD,
    (SDL_KEYUP, SDLK_a): AU,
}

#클래스를 이용해 상태를 만듬
class AUTO_RUN:
    @staticmethod
    def enter(self,event):
        print('AUTO_RUN ENTER')
        self.dir = self.face_dir


    @staticmethod
    def exit(self):
        self.face_dir = self.dir
        self.dir = 0

        print('AUTO_RUN EXIT')

    @staticmethod
    def do(self):
        self.frame = (self.frame+1 )%8
        print('AUTO_RUN DO')
        self.x += self.dir
        if self.x < 0: self.dir = 1
        elif self.x > 800 : self.dir = -1


    @staticmethod
    def draw(self):
        print('AUTO_RUN DRAW')
        if self.dir == -1:
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        elif self.dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)

class IDLE:
    @staticmethod
    def enter(self,event):
        print('IDLE ENTER')
        self.dir = 0
        self.timer = 1000

    @staticmethod
    def exit(self):
        print('IDLE EXIT')

    @staticmethod
    def do(self):
        self.frame = (self.frame+1 )%8
        print('IDLE DO')
        self.timer -= 1
        if self.timer == 0: #시간 초과
            #self.q.insert(0,TIMER) # 객체지향 프로그래밍에 위배됨 why ? q를 직접적으로 액세스 하기 때문에
            self.addEvent(TIMER)

    @staticmethod
    def draw(self):
        if self.face_dir == 1:
             self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
        else:
             self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)

class RUN:
    @staticmethod
    def enter(self,event):
        print('RUN ENTER')
        if event == RD : self.dir += 1
        elif event == LD : self.dir -= 1
        elif event == RU : self.dir -= 1
        elif event == LU : self.dir += 1


    @staticmethod
    def exit(self):
        print('RUN EXIT')
        #run이 나갈때 idle에게 run의 방향을 알려줄 필요가 있다.
        self.face_dir = self.dir

    @staticmethod
    def do(self):
        print('RUN DO')
        self.frame = (self.frame + 1) % 8
        self.x += self.dir
        self.x = clamp(0,self.x,800)

    @staticmethod
    def draw(self):
        print('RUN DRAW')
        if self.dir == -1:
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        elif self.dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)

class SLEEP:
    @staticmethod
    def enter(self,event):
        print('SLEEP ENTER')
        self.dir = 0


    @staticmethod
    def exit(self):
        print('SLEEP EXIT')

    @staticmethod
    def do(self):
        self.frame = (self.frame+1 )%8
        print('SLEEP DO')
    @staticmethod
    def draw(self):
        print('SLEEP DRAW')
        if self.face_dir == 1:
            self.image.clip_composite_draw(self.frame * 100 , 300 , 100,100,3.141592/2,'',self.x,self.y,100,100)
        else:
            self.image.clip_composite_draw(self.frame * 100, 200, 100, 100, -3.141592 / 2, '', self.x, self.y, 100, 100)


class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.image = load_image('animation_sheet.png')
        self.timer = 0

        self.q = []
        self.cur_state = IDLE
        self.cur_state.enter(self,None)

    def update(self):
        # self.frame = (self.frame + 1) % 8
        # self.x += self.dir * 1
        # self.x = clamp(0, self.x, 800)
        self.cur_state.do(self)

        if self.q:
            event = self.q.pop() #이벤트를 가져와
            self.cur_state.exit(self) # 현재상태를 나가고
            self.cur_state = next_state[self.cur_state][event] #다음 상태가 계산되면
            self.cur_state.enter(self,event) #다음상태를 실행

    def addEvent(self,event):
        self.q.insert(0, event)

    def handle_event(self,event): #소년 스스로 이벤트 처리
        #event 는 key이벤트 이것을 내부 RD 등으로 변환
        if(event.type , event.key) in key_event_table:
            key_event = key_event_table[(event.type,event.key)]
            self.addEvent(key_event) #변환된 내부이벤트를 큐에 추가
        # if event.type == SDL_KEYDOWN:
        #     match event.key:
        #         case pico2d.SDLK_LEFT:
        #             self.dir -= 1
        #         case pico2d.SDLK_RIGHT:
        #             self.dir += 1
        # elif event.type == SDL_KEYUP:
        #     match event.key:
        #         case pico2d.SDLK_LEFT:
        #             self.dir += 1
        #             self.face_dir = -1
        #         case pico2d.SDLK_RIGHT:
        #             self.dir -= 1
        #             self.face_dir = 1


    def draw(self):
        self.cur_state.draw(self)
        # if self.dir == -1:
        #     self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        # elif self.dir == 1:
        #     self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)
        # else:
        #     if self.face_dir == 1:
        #         self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
        #     else:
        #         self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)

next_state ={
    IDLE : {RU:RUN,LU:RUN,RD:RUN,LD:RUN,TIMER:SLEEP,AD:AUTO_RUN,AU:IDLE},
    RUN : {RU :IDLE,LU:IDLE,RD:IDLE,LD:IDLE,AD:AUTO_RUN},
    SLEEP : {RD:RUN , LD:RUN, RU:RUN,LU:RUN,AD:AUTO_RUN},
    AUTO_RUN: {AD: IDLE, AU: AUTO_RUN,RD:RUN,LD:RUN,RU:IDLE,LU:IDLE}
}