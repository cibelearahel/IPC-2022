import math
import turtle


iterations = int(input("Enter the number of iterations: "))
factor = 1


def fibonacci_plot(iterations):
    a, b = 0, 1
    square_a, square_b = a, b

    plot_pen.pencolor("blue")

    plot_pen.forward(b * factor)
    plot_pen.left(90)
    plot_pen.forward(b * factor)
    plot_pen.left(90)
    plot_pen.forward(b * factor)
    plot_pen.left(90)
    plot_pen.forward(b * factor)

    square_b = square_a + square_b
    square_a = square_b

    for i in range(1, iterations):
        plot_pen.backward(square_a * factor)
        plot_pen.right(90)
        plot_pen.forward(square_b * factor)
        plot_pen.left(90)
        plot_pen.forward(square_b * factor)
        plot_pen.left(90)
        plot_pen.forward(square_b * factor)

        square_b = square_a + square_b
        square_a = square_b

    plot_pen.penup()
    plot_pen.setposition(factor, 0)
    plot_pen.seth(0)
    plot_pen.pendown()

    plot_pen.pencolor("red")

    plot_pen.left(90)

    for i in range(iterations):
        print(b)
        spiral_plot = (math.pi * b * factor / 2) / 90
        for j in range(90):
            plot_pen.forward(spiral_plot)
            plot_pen.left(1)
        a, b = b, a + b


if iterations > 0:
    print("Fibonacci series for", iterations, "elements:")
    plot_pen = turtle.Turtle()
    plot_pen.speed(100)
    fibonacci_plot(iterations)
    turtle.done()
else:
    print("Number of iterations must be bigger than 0")
