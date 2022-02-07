import turtle

window = turtle.Screen()

triangle = turtle.Turtle()


def triangle_task(x, y):
    triangle.penup()

    triangle.goto(x, y)

    triangle.pendown()

    for i in range(3):
        triangle.forward(100)

        triangle.left(120)

        triangle.forward(100)


turtle.onscreenclick(triangle_task, 1)

turtle.listen()

turtle.done()
