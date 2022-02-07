from turtle import *

speed('fastest')

right(-90)

angle = 30


# function to plot a Y
def y_tree(size, level):
    if level > 0:
        colormode(255)

        pencolor(0, 255 // level, 0)

        # drawing the base
        forward(size)

        right(angle)

        # the right subtree
        y_tree(0.8 * size, level - 1)

        pencolor(0, 255 // level, 0)

        left(2 * angle)

        # the left subtree
        y_tree(0.8 * size, level - 1)

        pencolor(0, 255 // level, 0)

        right(angle)

        forward(-size)


# tree of size 80 and level 7
y_tree(80, 7)
