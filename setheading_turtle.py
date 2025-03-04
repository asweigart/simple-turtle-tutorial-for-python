# setheading_turtle.py

from turtle import *
import random

pensize(4)
left(random.randint(0, 360))
write(str(heading()), font=('Arial', 48, 'normal'))
forward(200)

setheading(45)
write(str(heading()), font=('Arial', 48, 'normal'))
forward(200)

done()
