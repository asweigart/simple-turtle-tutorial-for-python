# blue_flowers.py
from turtle import *
from random import *

tracer(100, 0)

for n in range(50):
    # Move to a random location:
    penup()
    x = randint(-300, 300)
    y = randint(-300, 300)
    goto(x, y)
    pendown()

    # Make a random blue color:
    pencolor((0, 0, random()))

    # Make a random pen thickness:
    pensize(randint(1, 5))

    # Make a random size for the circles:
    circle_size = randint(10, 40)

    # Draw six circles.
    for i in range(6):
        circle(circle_size)
        left(60)
update()
done()
