# solution_star_outline.py

from turtle import *

# Move the turtle to the first point of the star:
pensize(4)
penup()
goto(0, 300)

# Draw lines to the other points of the star:
pendown()
goto(70, 95)
goto(285, 95)
goto(110, -35)
goto(175, -260)
goto(0, -100)
goto(-175, -260)
goto(-110, -35)
goto(-285, 95)
goto(-70, 95)
goto(0, 300)

done()