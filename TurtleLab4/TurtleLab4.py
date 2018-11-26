import turtle

turtle.setup(width=750, height=700)
turtle.title('turtle drawing')
turtle.bgcolor ('black')
turtle.speed(50)
colors = ['#FF0000','#FF7100','#FFC600','#3EFF00','#00FFE9','#0078FF','#AB00FF','#FF0095']
turtle.color(colors)

def main():
    drawing()
    filled_arc()
    turtle.exitonclick()

def filled_arc(radius,angle,color):
    turtle.color(color)
    turtle.begin_fill()
    turtle.forward(90)
    turtle.circle(radius,angle)
    turtle.left(90)
    turtle.forward(radius)
    turtle.end_fill()
    turtle.left(180-angle)

angle = 360/len(colors)
for color in colors:
    filled_arc(100,angle,color)
    turtle.left(angle)

def drawing():
    for x in range(8):
        turtle.forward(x)
        turtle.circle(140)
        turtle.left(45)

main()
