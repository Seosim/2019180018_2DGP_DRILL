import turtle

cnt = 4

while cnt > 0:
    turtle.forward(300)
    turtle.left(90)
    cnt -= 1

cnt = 5

while cnt > 0:
    if cnt%2 == 1:
        turtle.forward(60)
        turtle.left(90)
        turtle.forward(300)
        turtle.right(90)
    else:
        turtle.forward(60)
        turtle.right(90)
        turtle.forward(300)
        turtle.left(90)
    cnt -= 1

cnt = 5
turtle.right(90)

while cnt > 0:
    if cnt%2 == 0:
        turtle.forward(60)
        turtle.left(90)
        turtle.forward(300)
        turtle.right(90)
    else:
        turtle.forward(60)
        turtle.right(90)
        turtle.forward(300)
        turtle.left(90)
    cnt -= 1



turtle.exitonclick()


    
