# solution_cube.py
from turtle import *
pensize(4)

# Front square:
for i in range(4):
    forward(200)
    right(90)

# Top left diagonal:
left(45)
forward(200)
right(45)

# Top side of back square:
forward(200)
right(135)
forward(200)
backward(200)
left(45)

# Right side of back square:
forward(200)
right(45)
forward(200)
backward(200)
right(45)

# Bottom side of back square:
forward(200)
left(45)
forward(200)
backward(200)

# Left side of back square:
right(135)
forward(200)

done()
