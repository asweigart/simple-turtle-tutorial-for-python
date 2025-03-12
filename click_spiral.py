# click_spiral.py
from turtle import *
from random import *

tracer(1000, 0)  # TODO

def draw_spiral(x, y):
    # Move to the XY coordinates of the mouse click:
    penup()
    goto(x, y)
    pendown()

    # Draw a spiral:
    setheading(0)
    line_length = randint(50, 200)
    turn_radius = randint(50, 70)
    for i in range(100):
        forward(i)
        left(turn_radius)
    update()

# Set the draw_spiral() function to be called when a click happens:
getscreen().onclick(draw_spiral)
done()