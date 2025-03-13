# draw_circles.py
from turtle import *

speed('fastest')

# Draw circle in the top half of the window:
setheading(0)  # Face right.
for i in range(20):
    circle(i * 10)

# Draw circles in the bottom half of the window:
setheading(180)  # Face left.
for i in range(20):
    circle(i * 10)

done()
