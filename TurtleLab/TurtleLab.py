import turtle

turtle.title('turtle drawing')
turtle.bgcolor ('black')
turtle.speed(500)

def main():
    line()
    square()
    circle()
    triangle()
    turtle.exitonclick()


def line():
    turtle.penup()
    turtle.goto(-50,0)
    turtle.pendown()
    turtle.color('red','yellow')
    turtle.forward(100)

def square():
    turtle.penup()
    turtle.goto(-100,-100)
    turtle.pendown()
    turtle.color('blue','white')
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(200)
    turtle.left(90)

def circle():
    turtle.penup()
    turtle.goto(0,-300)
    turtle.pendown()
    turtle.color('#ffe063')
    turtle.circle(300)

def triangle():
    turtle.penup()
    turtle.goto(-200,-135)
    turtle.pendown()
    turtle.color(1.0,2.0,0.0)
    turtle.forward(400)
    turtle.left(120)
    turtle.forward(400)
    turtle.left(120)
    turtle.forward(400)
    turtle.left(120)




main()
