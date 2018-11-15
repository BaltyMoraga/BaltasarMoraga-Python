import turtle

turtle.setup(width=750, height=700)
turtle.title('turtle drawing')
turtle.bgcolor ('black')
turtle.speed(5)

def main():
    poly()
    turtle.exitonclick()

def poly():
    color = ((1.0,1.0,1.0),(1.0,0.0,1.0),(1.0,1.0,0.0),(0.8,0.9,1.0),(0.0,0.0,1.0))
    turtle.color(color)
    turtle.penup()
    turtle.goto(-100,-200)
    turtle.pendown()
    for x in range(8):
        turtle.forward(200)
        turtle.left(45)

main()
