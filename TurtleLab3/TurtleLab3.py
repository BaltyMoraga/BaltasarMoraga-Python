import turtle

turtle.setup(width=750, height=700)
turtle.title('turtle drawing')
turtle.bgcolor ('black')
turtle.speed(10)

def main():
    square()
    triangle()
    poly()
    poly2()
    turtle.exitonclick()

def square():
    turtle.color('#00FFE8')
    turtle.penup()
    turtle.goto(-300,-260)
    turtle.pendown()
    for x in range(4):
        turtle.forward(200)
        turtle.left(90)

def triangle():
    turtle.color('#FFAD3C')
    turtle.penup()
    turtle.goto(-300,100)
    turtle.pendown()
    for x in range(3):
        turtle.forward(200)
        turtle.left(120)

def poly():
    turtle.color('#FF2B2B')
    turtle.penup()
    turtle.goto(150,-260)
    turtle.pendown()
    for x in range(10):
        turtle.forward(75)
        turtle.left(36)

def poly2():
    turtle.color('#29FF0C')
    turtle.penup()
    turtle.goto(150,70)
    turtle.pendown()
    for x in range(15):
        turtle.forward(50)
        turtle.left(24)

main()
