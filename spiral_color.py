from turtle import *
import random

colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']

speed('fastest')
for x in range(300):
    pencolor(random.choice(colors))
    forward(x)
    left(91)
done()