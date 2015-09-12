# A Simple Tutorial for Python's turtle.py Module

## Introduction

Turtle graphics is a popular way for introducing programming to kids. It was part of the original Logo programming language developed by Wally Feurzig and Seymour Papert in 1966.

The user is given a two-dimensional area with "turtles". Each turtle can be programmed to move around the world while drawing a line behind it. When we say turtle, we mean the programmable object that is in the two-dimensional world. The "turtle" could look like the turtle animal, an arrow, or be invisibile.

By programming the turtle to move around and draw, the user can write programs that draw beautiful shapes.

## Some Examples

A square spiral program:

```python
import turtle
for i in range(500):
    turtle.forward(i)
    turtle.left(91)
```

The square spiral output:


A colorful hexagon spiral program:

```python
import turtle
colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
for x in range(360):
    turtle.pencolor(colors[x % 6])
    turtle.width(x / 100 + 1)
    turtle.forward(x)
    turtle.left(59)
```

The colorful hexagon spiral output:


A blue flowers program:

```python
import turtle
import random

for n in range(60):
    turtle.penup()
    turtle.goto(random.randint(-400, 400), random.randint(-400, 400))
    turtle.pendown()

    red_amount = random.randint(0, 30) / 100.0
    blue_amount = random.randint(50, 100) / 100.0
    green_amount = random.randint(0, 30) / 100.0
    turtle.pencolor((red_amount, green_amount, blue_amount))

    circle_size = random.randint(10, 40)
    turtle.pensize(random.randint(1, 5))

    for i in range(6):
        turtle.circle(circle_size)
        turtle.left(60)
```

The blue flowers output:


## Beginning with turtle.py




## Moving

### forward()

### backward()

### right()

### left()

### goto()

### setx()

### sety()

### setdirection()

### undo()

### home()



## Drawing

### pendown()

### penup()

### pensize()

### pencolor()

### clear()

### reset()




## Filling in Shapes

### fillcolor()

### begin_fill()

### end_fill()




## Stamping

### stamp()

### clearstamp()

### clearstamps()



## Animation

### speed()

## Turtle Status

### position()

### towards()

### distance()

### degrees()

### radians()

### isdown()

### isvisible()


## Input




## Events

### listen()

### onkey()

### onkeypress()

### onclick()

### ontimer()

### done()

### exitonclick()



## The Turtle

### showturtle()

### hideturtle()

### shape()


## The World

### bgcolor()

### bgpic()

### title()

### screensize()

### window_height()

### window_width()

### listen()