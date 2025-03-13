# solution_cross_setheading.py

from turtle import *

pensize(4)

# Right bump:
setheading(0)  # Face right.
forward(100)
setheading(270)  # Face down.
forward(100)
setheading(180)  # Face left.
forward(100)

# Bottom bump:
setheading(270)  # Face down.
forward(100)
setheading(180)  # Face left.
forward(100)
setheading(90)  # Face up.
forward(100)

# Left bump:
setheading(180)  # Face left.
forward(100)
setheading(90)  # Face up.
forward(100)
setheading(0)  # Face right.
forward(100)

# Top bump:
setheading(90)  # Face up.
forward(100)
setheading(0)  # Face right.
forward(100)
setheading(270)  # Face down.
forward(100)

done()
