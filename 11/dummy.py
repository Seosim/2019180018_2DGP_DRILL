# class Star: #객체 생성용이 아닌 그룹핑 용도
#     type = 'star'
#     x = 100
#
#     def change():
#         x = 200
#         print('x =' ,x)
#
# print('x is' ,Star.x)
# Star.change()
#
# star = Star() #굳이 객체를 생성하는것도 가능
# print(star.x) # 객체 변수로 액세스하지만 클래스 x를 가르킨다
# star.change()

# class Player:
#     name = 'player'
#
#     def __init__(self):
#         self.x = 100
#
#     def where(self):
#         print(self.x)
#
# player = Player()
# player.where() # --> Player.where(player) 와 동일
#
# print(Player.name) # 클래스 변수 출력
# print(player.name)  # name이라는 객체 변수가 없으면 같은 이름의 클래스 변수가 선택됨
#
# Player.where(player) # 이게 원칙적인 파이썬에서의 멤버함수 호출

table = {
    'SLEEP' : {'HIT' : 'WAKE'},
    'WAKE' : {'TIMER10' : 'SLEEP'}
}

cur_state = 'SLEEP'
next_state = table[cur_state]['HIT']