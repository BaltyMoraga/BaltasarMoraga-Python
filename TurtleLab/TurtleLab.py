import turtle

turtle.setup(width=750, height=700)
turtle.title('turtle drawing')
turtle.bgcolor ('black')
turtle.speed(50)

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
    turtle.goto(-200,-130)
    turtle.pendown()
    turtle.color(0.1,1.0,0.6)
    turtle.forward(400)
    turtle.left(120)
    turtle.forward(400)
    turtle.left(120)
    turtle.forward(400)
    turtle.left(120)

main()
