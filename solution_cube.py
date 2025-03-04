# solution_cross.py

from turtle import *

# Front square:
for i in range(4):
    forward(100)
    right(90)

# Top left diagonal:
left(45)
forward(100)
right(45)

# Top side of back square:
forward(100)
right(135)
forward(100)
backward(100)
left(45)

# Right side of back square:
forward(100)
right(45)
forward(100)
backward(100)
right(45)

# Bottom side of back square:
forward(100)
left(45)
forward(100)
backward(100)

# Left side of back square:
right(135)
forward(100)

done()
