# solution_fan.py
from turtle import *
from random import *
pensize(4)
speed('fastest')

for i in range(10):
    goto(randint(-400, 400), randint(-400, 400))
    setheading(randint(0, 360))
    forward(100)
    home()

done()
