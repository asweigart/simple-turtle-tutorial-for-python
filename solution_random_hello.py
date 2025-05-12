# solution_random_hello.py
from turtle import *
from random import *

tracer(1000, 0)
penup()
hideturtle()

for i in range(100):
    goto(randint(-400, 400), randint(-400, 400))
    write('Hello, world!', font=('Arial', randint(12, 48), 'normal'))

update()
done()
