import turtle

turtle.color('red')
turtle.bgcolor('black')
def main():
    square()
    rectangle()
    turtle.exitonclick()

def square():
    turtle.forward(75)
    turtle.left(90)
    turtle.forward(75)
    turtle.left(90)
    turtle.forward(75)
    turtle.left(90)
    turtle.forward(75)
    turtle.left(90)
    turtle.penup()
    turtle.goto(0,100)
    turtle.pendown()
    turtle.forward(75)
    turtle.left(90)
    turtle.forward(75)
    turtle.left(90)
    turtle.forward(75)
    turtle.left(90)
    turtle.forward(75)
    turtle.left(90)

def rectangle():
    turtle.penup
    turtle.goto(-100,0)
    turtle.pendown
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)

main()
