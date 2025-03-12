# spiral_color.py
from turtle import *
from random import *

colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']

speed('fastest')
for x in range(300):
    pencolor(choice(colors))
    forward(x)
    left(91)
hideturtle()
done()