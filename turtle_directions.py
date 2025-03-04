# turtle_directions.py
from turtle import *

for i in range(24):
    forward(200)  # Move forward in the current direction.
    write(str(heading()))  # Write the degrees of the direction.
    backward(200)  # Move back to the center.
    left(15)  # Turn left by 15 degrees and repeat.
done()