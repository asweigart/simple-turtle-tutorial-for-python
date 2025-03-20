# square_random.py
from turtle import *
from random import *

pensize(4)
speed('fastest')

for i in range(50):
    forward(200)
    # Turn left a random number of degrees between 80 and 100:
    left(randint(85, 95))
hideturtle()
done()