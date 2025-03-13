# colorful_squares.py

from turtle import *
from random import *

pensize(4)
tracer(10, 0)

for i in range(100):  # Draw 100 squares.
    # Move to a random place:
    penup()
    goto(randint(-400, 200), randint(-400, 200))
    pendown()

    # Set fill and pen colors to something random:
    fillcolor((random(), random(), random()))
    pencolor((random(), random(), random()))

    # Make the square size random:
    line_length = randint(20, 200)

    # Draw the filled-in square:
    begin_fill()
    for j in range(4):
        forward(line_length)
        left(90)
    end_fill()

done()