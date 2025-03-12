# click_square.py
from turtle import *

speed('fastest')

def draw_square(x, y):
    # Move to the XY coordinates of the mouse click:
    penup()
    goto(x, y)
    pendown()

    # Draw a square:
    for i in range(4):
        forward(100)
        left(90)

# Set the draw_square() function to be called when a click happens:
getscreen().onclick(draw_square)  # NOTE: There is no () after draw_square
done()
