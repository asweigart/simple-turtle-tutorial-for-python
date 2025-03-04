# random_position.py
from turtle import *
from random import *

for i in range(8):
    write(str(position()))
    left(randint(0, 90))
    forward(100)

done()
