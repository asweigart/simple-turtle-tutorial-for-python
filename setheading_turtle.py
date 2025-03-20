# setheading_turtle.py

from turtle import *
from random import *

pensize(4)
left(randint(0, 360))
write(heading(), font=('Arial', 48, 'normal'))
forward(200)

setheading(45)
write(heading(), font=('Arial', 48, 'normal'))
forward(200)

done()
