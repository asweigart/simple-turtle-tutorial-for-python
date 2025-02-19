from turtle import *
import random

colors = ['red', 'orange', 'yellow', 'blue', 'green', 'purple']

speed('fastest')
pensize(3)
bgcolor('black')
for i in range(300):
    pencolor(random.choice(colors))
    forward(i)
    left(91)
done()
