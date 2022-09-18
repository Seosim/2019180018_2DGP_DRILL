import turtle
import random

def restart():
    turtle.reset()

def Up():
    x , y = turtle.position()
    turtle.goto(x,y+50)
    turtle.stamp()

def Down():
    x , y = turtle.position()
    turtle.goto(x,y-50)
    turtle.stamp()

def Left():
    x , y = turtle.position()
    turtle.goto(x-50,y)
    turtle.stamp()

def Right():
    x , y = turtle.position()
    turtle.goto(x+50,y)
    turtle.stamp()
    
    
turtle.shape("turtle")

turtle.onkey(Up, 'w')
turtle.onkey(Down, 's')
turtle.onkey(Left,'a')
turtle.onkey(Right,'d')
turtle.onkey(restart,'Escape')

turtle.listen()






