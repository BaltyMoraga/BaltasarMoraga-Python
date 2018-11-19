import turtle

turtle.setup(width=750, height=700)
turtle.title('turtle drawing')
turtle.bgcolor ('black')
turtle.speed(50)

def main():
    drawing()
    turtle.exitonclick()

def drawing():
    turtle.color('red')
    for x in range(1000):
        turtle.forward(x)
        turtle.left(150)
        turtle.left(39)

main()
