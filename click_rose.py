# click_rose.py
from turtle import *
from random import *

tracer(1000, 0)
bgcolor('black')
hideturtle()

def draw_rose(x, y):
    # Move to the XY coordinates of the mouse click:
    penup()
    goto(x, y)
    pendown()

    # Draw a red rose bud:
    for i in range(100):
        # Set random pen color and size for each line:
        pencolor((random(), 0, 0))
        pensize(randint(2, 5))
        forward(i)
        left(randint(50, 70))
    update()


# Set the draw_rose() function to be called when a click happens:
getscreen().onclick(draw_rose)

done()