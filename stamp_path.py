# stamp_path.py
from turtle import *
from random import *

shape('turtle')
speed('fastest')
penup()
bgcolor((0.1, 0.6, 0.8))  # Set the background color to a light blue.

start_heading = 0
while start_heading < 360:
    home()
    setheading(start_heading)
    pencolor('white')
    fillcolor(choice(['green', 'yellow']))
    for j in range(12):
        left(randint(-20, 20))  # Randomly turn up to 20 degrees left or right.
        forward(30)  # 30 step gap in between stamps.
        stamp()
    start_heading = start_heading + 20

done()
