# turtle_directions.py
from turtle import *

for i in range(24):
    forward(200)  # Move forward in the current direction.
    write(heading(), font=('Arial', 12, 'normal'))  # Write the degrees of the direction.
    backward(200)  # Move back to the center.
    left(15)  # Turn left by 15 degrees and repeat.
done()