# square_random.py
from turtle import *
import random

speed('fastest')
for i in range(50):
    forward(100)
    # Turn left a random number of degrees between 80 and 100:
    left(random.randint(80, 100))
hideturtle()
done()
