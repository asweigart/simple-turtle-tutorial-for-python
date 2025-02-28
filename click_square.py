# click_square.py
from turtle import *

speed('fastest')

def draw_square(x, y):
    goto(x, y)  # TODO
    for i in range(4):
        forward(100)
        left(90)

# When the turtle window is clicked, call draw_square():
getscreen().onclick(draw_square)
done()
