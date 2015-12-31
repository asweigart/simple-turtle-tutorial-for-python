<meta charset="UTF-8">
<link rel="stylesheet" type="text/css" href="simple_turtle_tutorial.css">

# A Simple Tutorial for Python's turtle.py Module

## Table of Contents

1. [Introduction](#introduction)
1. [Examples](#examples)
1. [Beginning with turtle.py](#beginning-with-turtle.py)
1. [Moving](#moving)
1. [Drawing](#drawing)
1. [Color](#color)
1. [Filling in Shapes](#filling-in-shapes)
1. [Stamping](#stamping)
1. [Animation](#animation)
1. [Turtle Status](#turtle-status)
1. [Input](#input)
1. [Events](#events)
1. [The Turtle](#the-turtle)
1. [The World](#the-world)

## Introduction

Turtle graphics is a popular way for introducing programming to kids. Virtual turtles can be programmed to move around the screen. The turtle draws lines as it moves. The "turtle" could look like the turtle animal, an arrow, or be invisibile. The user can write turtle programs that draw beautiful shapes and learn to program at the same time.

The original Turtle software was developed by Wally Feurzig and Seymour Papert in 1966.

This tutorial only explains Python's turtle.py module. It does not explain the Python programming language.

## Quickstart

TODO - explain how to install python, run IDLE

In IDLE, click on File > New File. Then enter the following:

```python
from turtle import *

forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
```

Click on File > Save and save this program. Then press F5 to run the program. The output of this program will look like this:

[<img src="square.png" class="screenshot" />](square_spiral.png)

The instructions in your program tell the "turtle" how to move. The turtle draws a line behind it as it moves. This program draws a square. The steps given to the program are:

1. Move forward 100 steps. (In the beginning, the turtle is facing to the right.)
1. Turn 90 degrees to the left.
1. Move forward 100 steps.
1. Turn 90 degrees to the left.
1. Move forward 100 steps.
1. Turn 90 degrees to the left.
1. Move forward 100 steps. The turtle has ended up where it started.

With these seven steps, the turtle draws a square. The `from turtle import *` is an instruction needed at the beginning of all of your turtle programs. It imports the turtle module so you can do the turtle instructions.

There are many instructions like left() and forward(). These instructions are called functions. This tutorial explains many of the functions in the turtle module. When you learn more of these functions, you will be able to draw many different shapes and beautiful pictures!

## Examples

A square spiral program:

```python
from turtle import *
for i in range(500): # this "for" loop will repeat these functions 500 times
    forward(i)
    left(91)
```

[<img src="square_spiral.png" class="screenshot" />](square_spiral.png)

A colorful hexagon spiral program:

```python
from turtle import *
colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
for x in range(360):
    pencolor(colors[x % 6])
    width(x / 100 + 1)
    forward(x)
    left(59)
```

[<img src="colorful_hex.png" class="screenshot" />](colorful_hex.png)

A blue flowers program:

```python
from turtle import *
import random

for n in range(60):
    penup()
    goto(random.randint(-400, 400), random.randint(-400, 400))
    pendown()

    red_amount   = random.randint( 0,  30) / 100.0
    blue_amount  = random.randint(50, 100) / 100.0
    green_amount = random.randint( 0,  30) / 100.0
    pencolor((red_amount, green_amount, blue_amount))

    circle_size = random.randint(10, 40)
    pensize(random.randint(1, 5))

    for i in range(6):
        circle(circle_size)
        left(60)
```

[<img src="blue_flowers.png" class="screenshot" />](blue_flowers.png)

## Moving

By calling these functions, the turtle can be made to move around the screen. Imagine the turtle holding a pen down on the ground and drawing a line as it moves around.

The turtle's position is two numbers: the X coordinate and Y coordinate. The turtle also

### forward(*distance*)

The forward() function moves the turtle *distance* number of steps in the current direction. If the pen is down (see pendown() and penup()) a line will be drawn as the turtle moves forward. If *distance* is a negative number, the turtle will move backwards.

### backward(*distance*)

The backward() function moves the turtle *distance* number of steps in **opposite direction** the current direction. If the pen is down (see pendown() and penup()) a line will be drawn as the turtle moves backward. If *distance* is a negative number, the turtle will move forward.

### right(*angle*)

The right() function will change the current direction clockwise by *angle* degrees. If you imagine being above the turtle looking down, the turtle turning right looks like it is turning clockwise. The turtle will not move; it will only change the direction it is facing.

This example moves the turtle forward, then turns right by 90 degrees, then moves forward again:

This example moves the turtle forward, then turns left by 90 degrees, then moves forward again:

```python
from turtle import *
forward(100)
right(90)
forward(100)
```

[<img src="turn_right.png" class="screenshot" />](turn_right.png)

### left(*angle*)

The left() function will change the current direction counter-clockwise or anti-clockwise by *angle* degrees. If you imagine being above the turtle looking down, the turtle turning left looks like it is turning counter-clockwise or anti-clockwise. The turtle will not move; it will only change the direction it is facing.

This example moves the turtle forward, then turns left by 90 degrees, then moves forward again:

```python
from turtle import *
forward(100)
left(90)
forward(100)
```

[<img src="turn_left.png" class="screenshot" />](turn_left.png)

### goto(*x*, *y*)

The goto() function will immediately move the turtle to the given *x* and *y* coordinates. If the pen is down (see pendown() and penup()) a line will be drawn from the previous coordinates to the new coordinates.

This example moves the to several x and y coordinates while drawing a line behind it:

```python
from turtle import *

goto(50, 50)
goto(-50, 50)
goto(100, -50)
goto(-50, -50)
```

[<img src="goto.png" class="screenshot" />](goto.png)

### setx(*x*)

The goto() function will immediately move the turtle to the given *x* coordinate. The turtle's y coordinate will stay the same. If the pen is down (see pendown() and penup()) a line will be drawn from the previous coordinates to the new coordinates.

### sety(*y*)

The goto() function will immediately move the turtle to the given *y *coordinate. The turtle's x coordinate will stay the same. If the pen is down (see pendown() and penup()) a line will be drawn from the previous coordinates to the new coordinates.

### setheading(*heading*)

The setheading() function will change the current direction to the *heading* angle. If you imagine being above the turtle looking down, the turtle turning left looks like it is turning counter-clockwise or anti-clockwise. The turtle will not move; it will only change the heading it is facing.

```python
from turtle import *

for angle in range(0, 360, 15):
    setheading(angle)
    forward(100)
    write(str(angle) + '°')
    backward(100)
```

[<img src="setheading.png" class="screenshot" />](setheading.png)

### undo()

The undo() function will undo the turtle's last action. It will be as though the last action was never made. For example, if the last action was a call to the forward(100) function, calling undo will move the turtle backwards 100 steps and erase any line that was drawn. The undo() function can be called many times to erase more and more of the turtle

```python
from turtle import *

for i in range(10):
    forward(100)
    left(90)
    forward(10)
    left(90)
    forward(100)
    right(90)
    forward(10)
    right(90)

for i in range(30):
    undo()
```

[<img src="undo_before.png" class="screenshot" />](undo_before.png) [<img src="undo_after.png" class="screenshot" />](undo_after.png)


### home()

The home() function will move the turtle to it's original position at the coordinates (0, 0) and set it's direction to 0 degrees. Calling home() is the same as calling goto(0, 0) and setheading(0). If the pen is down (see pendown() and penup()) a line will be drawn as the turtle moves back home.

```python
from turtle import *

forward(100)
right(90)
forward(100)
home()
```

[<img src="home.png" class="screenshot" />](home.png)

## Drawing

### pendown()

The pendown() function will cause the turtle to draw as it moves around. The line it draws can be set with the pencolor() and pensize() functions.

### penup()

The penup() function will cause the turtle to draw as it moves around. The line it draws can be set with the pencolor() and pensize() functions.

### pensize(*size*)

The pensize() function sets the width of the line that the turtle draws as it moves.

[<img src="pensize.png" class="screenshot" />](pensize.png)

### pencolor(), pencolor(*color*), pencolor((*red*, *green*, *blue*)), pencolor(*red*, *green*, *blue*)

The pencolor() function sets the color of the line that the turtle draws. The pencolor() function can be passed a string of the color, such as 'red' or 'black'. Or, the pencolor() function can be passed an "RGB color tuple" (see the [Color](#color) section).

```python
from turtle import *

pensize(20)
pencolor('red')
forward(50)
pencolor(0, 1.0, 0)
forward(50)
pencolor((0, 0.5, 0.5))
forward(50)

pensize(10)
goto(-400, 50)

for red in range(4):
    for green in range(4):
        for blue in range(4):
            pencolor(red / 4.0, green / 4.0, blue / 4.0)
            forward(10)
```

[<img src="pencolor.png" class="screenshot" />](pencolor.png)

### clear()

The clear() function will erase all the line drawings on the screen. This function does not move the turtle.

### reset()

The reset()) function will erase all the line drawings on the screen and return the turtle to the (0, 0) coordinate and facing 0 degrees. This function does the same thing as calling the clear() and home() function.

## Color

Red, green, and blue are the three primary colors of light.

The float value 0.0 represents no brightness of that color. The float value 1.0 represents full brightness of that color. So the color red is represented by the RGB color tuple (1.0, 0, 0). The color purple is half-bright red and half-bright blue, so it is represented by the RGB color tuple (0.5, 0.0, 0.5). Full brightness of red and blue makes pink: (1.0, 0.0, 1.0)

Move the mouse over these colors to view their RGB colortuples:

<script type="text/javascript">
function setColor(color)
{
var iLen = String(color).length;
color = String(color).substring(iLen, iLen - 6);
r = parseInt( String(color).substring(0,2), 16 ) / 255;
g = parseInt( String(color).substring(2,4), 16 ) / 255;
b = parseInt( String(color).substring(4,6), 16 ) / 255;
document.getElementById("RGBTupleField").value = "(" + r.toFixed(2) + ", " + g.toFixed(2) + ", " + b.toFixed(2) + ")";
};
</script>

<table>
<tbody><tr>
<td class="color_td" style="background:#330000" onmouseover="setColor('#330000')">&nbsp;</td>
<td class="color_td" style="background:#331900" onmouseover="setColor('#331900')">&nbsp;</td>
<td class="color_td" style="background:#333300" onmouseover="setColor('#333300')">&nbsp;</td>
<td class="color_td" style="background:#193300" onmouseover="setColor('#193300')">&nbsp;</td>
<td class="color_td" style="background:#003300" onmouseover="setColor('#003300')">&nbsp;</td>
<td class="color_td" style="background:#003319" onmouseover="setColor('#003319')">&nbsp;</td>
<td class="color_td" style="background:#003333" onmouseover="setColor('#003333')">&nbsp;</td>
<td class="color_td" style="background:#001933" onmouseover="setColor('#001933')">&nbsp;</td>
<td class="color_td" style="background:#000033" onmouseover="setColor('#000033')">&nbsp;</td>
<td class="color_td" style="background:#190033" onmouseover="setColor('#190033')">&nbsp;</td>
<td class="color_td" style="background:#330033" onmouseover="setColor('#330033')">&nbsp;</td>
<td class="color_td" style="background:#330019" onmouseover="setColor('#330019')">&nbsp;</td>
<td class="color_td" style="background:#000000" onmouseover="setColor('#000000')">&nbsp;</td>
</tr>
<tr>
<td class="color_td" style="background:#660000" onmouseover="setColor('#660000')">&nbsp;</td>
<td class="color_td" style="background:#663300" onmouseover="setColor('#663300')">&nbsp;</td>
<td class="color_td" style="background:#666600" onmouseover="setColor('#666600')">&nbsp;</td>
<td class="color_td" style="background:#336600" onmouseover="setColor('#336600')">&nbsp;</td>
<td class="color_td" style="background:#006600" onmouseover="setColor('#006600')">&nbsp;</td>
<td class="color_td" style="background:#006633" onmouseover="setColor('#006633')">&nbsp;</td>
<td class="color_td" style="background:#006666" onmouseover="setColor('#006666')">&nbsp;</td>
<td class="color_td" style="background:#003366" onmouseover="setColor('#003366')">&nbsp;</td>
<td class="color_td" style="background:#000066" onmouseover="setColor('#000066')">&nbsp;</td>
<td class="color_td" style="background:#330066" onmouseover="setColor('#330066')">&nbsp;</td>
<td class="color_td" style="background:#660066" onmouseover="setColor('#660066')">&nbsp;</td>
<td class="color_td" style="background:#660033" onmouseover="setColor('#660033')">&nbsp;</td>
<td class="color_td" style="background:#202020" onmouseover="setColor('#202020')">&nbsp;</td>
</tr>
<tr>
<td class="color_td" style="background:#990000" onmouseover="setColor('#990000')">&nbsp;</td>
<td class="color_td" style="background:#994C00" onmouseover="setColor('#994C00')">&nbsp;</td>
<td class="color_td" style="background:#999900" onmouseover="setColor('#999900')">&nbsp;</td>
<td class="color_td" style="background:#4C9900" onmouseover="setColor('#4C9900')">&nbsp;</td>
<td class="color_td" style="background:#009900" onmouseover="setColor('#009900')">&nbsp;</td>
<td class="color_td" style="background:#00994C" onmouseover="setColor('#00994C')">&nbsp;</td>
<td class="color_td" style="background:#009999" onmouseover="setColor('#009999')">&nbsp;</td>
<td class="color_td" style="background:#004C99" onmouseover="setColor('#004C99')">&nbsp;</td>
<td class="color_td" style="background:#000099" onmouseover="setColor('#000099')">&nbsp;</td>
<td class="color_td" style="background:#4C0099" onmouseover="setColor('#4C0099')">&nbsp;</td>
<td class="color_td" style="background:#990099" onmouseover="setColor('#990099')">&nbsp;</td>
<td class="color_td" style="background:#99004C" onmouseover="setColor('#99004C')">&nbsp;</td>
<td class="color_td" style="background:#404040" onmouseover="setColor('#404040')">&nbsp;</td>
</tr>
<tr>
<td class="color_td" style="background:#CC0000" onmouseover="setColor('#CC0000')">&nbsp;</td>
<td class="color_td" style="background:#CC6600" onmouseover="setColor('#CC6600')">&nbsp;</td>
<td class="color_td" style="background:#CCCC00" onmouseover="setColor('#CCCC00')">&nbsp;</td>
<td class="color_td" style="background:#66CC00" onmouseover="setColor('#66CC00')">&nbsp;</td>
<td class="color_td" style="background:#00CC00" onmouseover="setColor('#00CC00')">&nbsp;</td>
<td class="color_td" style="background:#00CC66" onmouseover="setColor('#00CC66')">&nbsp;</td>
<td class="color_td" style="background:#00CCCC" onmouseover="setColor('#00CCCC')">&nbsp;</td>
<td class="color_td" style="background:#0066CC" onmouseover="setColor('#0066CC')">&nbsp;</td>
<td class="color_td" style="background:#0000CC" onmouseover="setColor('#0000CC')">&nbsp;</td>
<td class="color_td" style="background:#6600CC" onmouseover="setColor('#6600CC')">&nbsp;</td>
<td class="color_td" style="background:#CC00CC" onmouseover="setColor('#CC00CC')">&nbsp;</td>
<td class="color_td" style="background:#CC0066" onmouseover="setColor('#CC0066')">&nbsp;</td>
<td class="color_td" style="background:#606060" onmouseover="setColor('#606060')">&nbsp;</td>
</tr>
<tr>
<td class="color_td" style="background:#FF0000" onmouseover="setColor('#FF0000')">&nbsp;</td>
<td class="color_td" style="background:#FF8000" onmouseover="setColor('#FF8000')">&nbsp;</td>
<td class="color_td" style="background:#FFFF00" onmouseover="setColor('#FFFF00')">&nbsp;</td>
<td class="color_td" style="background:#80FF00" onmouseover="setColor('#80FF00')">&nbsp;</td>
<td class="color_td" style="background:#00FF00" onmouseover="setColor('#00FF00')">&nbsp;</td>
<td class="color_td" style="background:#00FF80" onmouseover="setColor('#00FF80')">&nbsp;</td>
<td class="color_td" style="background:#00FFFF" onmouseover="setColor('#00FFFF')">&nbsp;</td>
<td class="color_td" style="background:#0080FF" onmouseover="setColor('#0080FF')">&nbsp;</td>
<td class="color_td" style="background:#0000FF" onmouseover="setColor('#0000FF')">&nbsp;</td>
<td class="color_td" style="background:#7F00FF" onmouseover="setColor('#7F00FF')">&nbsp;</td>
<td class="color_td" style="background:#FF00FF" onmouseover="setColor('#FF00FF')">&nbsp;</td>
<td class="color_td" style="background:#FF007F" onmouseover="setColor('#FF007F')">&nbsp;</td>
<td class="color_td" style="background:#808080" onmouseover="setColor('#808080')">&nbsp;</td>
</tr>
<tr>
<td class="color_td" style="background:#FF3333" onmouseover="setColor('#FF3333')">&nbsp;</td>
<td class="color_td" style="background:#FF9933" onmouseover="setColor('#FF9933')">&nbsp;</td>
<td class="color_td" style="background:#FFFF33" onmouseover="setColor('#FFFF33')">&nbsp;</td>
<td class="color_td" style="background:#99FF33" onmouseover="setColor('#99FF33')">&nbsp;</td>
<td class="color_td" style="background:#33FF33" onmouseover="setColor('#33FF33')">&nbsp;</td>
<td class="color_td" style="background:#33FF99" onmouseover="setColor('#33FF99')">&nbsp;</td>
<td class="color_td" style="background:#33FFFF" onmouseover="setColor('#33FFFF')">&nbsp;</td>
<td class="color_td" style="background:#3399FF" onmouseover="setColor('#3399FF')">&nbsp;</td>
<td class="color_td" style="background:#3333FF" onmouseover="setColor('#3333FF')">&nbsp;</td>
<td class="color_td" style="background:#9933FF" onmouseover="setColor('#9933FF')">&nbsp;</td>
<td class="color_td" style="background:#FF33FF" onmouseover="setColor('#FF33FF')">&nbsp;</td>
<td class="color_td" style="background:#FF3399" onmouseover="setColor('#FF3399')">&nbsp;</td>
<td class="color_td" style="background:#A0A0A0" onmouseover="setColor('#A0A0A0')">&nbsp;</td>
</tr>
<tr>
<td class="color_td" style="background:#FF6666" onmouseover="setColor('#FF6666')">&nbsp;</td>
<td class="color_td" style="background:#FFB266" onmouseover="setColor('#FFB266')">&nbsp;</td>
<td class="color_td" style="background:#FFFF66" onmouseover="setColor('#FFFF66')">&nbsp;</td>
<td class="color_td" style="background:#B2FF66" onmouseover="setColor('#B2FF66')">&nbsp;</td>
<td class="color_td" style="background:#66FF66" onmouseover="setColor('#66FF66')">&nbsp;</td>
<td class="color_td" style="background:#66FFB2" onmouseover="setColor('#66FFB2')">&nbsp;</td>
<td class="color_td" style="background:#66FFFF" onmouseover="setColor('#66FFFF')">&nbsp;</td>
<td class="color_td" style="background:#66B2FF" onmouseover="setColor('#66B2FF')">&nbsp;</td>
<td class="color_td" style="background:#6666FF" onmouseover="setColor('#6666FF')">&nbsp;</td>
<td class="color_td" style="background:#B266FF" onmouseover="setColor('#B266FF')">&nbsp;</td>
<td class="color_td" style="background:#FF66FF" onmouseover="setColor('#FF66FF')">&nbsp;</td>
<td class="color_td" style="background:#FF66B2" onmouseover="setColor('#FF66B2')">&nbsp;</td>
<td class="color_td" style="background:#C0C0C0" onmouseover="setColor('#C0C0C0')">&nbsp;</td>
</tr>
<tr>
<td class="color_td" style="background:#FF9999" onmouseover="setColor('#FF9999')">&nbsp;</td>
<td class="color_td" style="background:#FFCC99" onmouseover="setColor('#FFCC99')">&nbsp;</td>
<td class="color_td" style="background:#FFFF99" onmouseover="setColor('#FFFF99')">&nbsp;</td>
<td class="color_td" style="background:#CCFF99" onmouseover="setColor('#CCFF99')">&nbsp;</td>
<td class="color_td" style="background:#99FF99" onmouseover="setColor('#99FF99')">&nbsp;</td>
<td class="color_td" style="background:#99FFCC" onmouseover="setColor('#99FFCC')">&nbsp;</td>
<td class="color_td" style="background:#99FFFF" onmouseover="setColor('#99FFFF')">&nbsp;</td>
<td class="color_td" style="background:#99CCFF" onmouseover="setColor('#99CCFF')">&nbsp;</td>
<td class="color_td" style="background:#9999FF" onmouseover="setColor('#9999FF')">&nbsp;</td>
<td class="color_td" style="background:#CC99FF" onmouseover="setColor('#CC99FF')">&nbsp;</td>
<td class="color_td" style="background:#FF99FF" onmouseover="setColor('#FF99FF')">&nbsp;</td>
<td class="color_td" style="background:#FF99CC" onmouseover="setColor('#FF99CC')">&nbsp;</td>
<td class="color_td" style="background:#E0E0E0" onmouseover="setColor('#E0E0E0')">&nbsp;</td>
</tr>
<tr>
<td class="color_td" style="background:#FFCCCC" onmouseover="setColor('#FFCCCC')">&nbsp;</td>
<td class="color_td" style="background:#FFE5CC" onmouseover="setColor('#FFE5CC')">&nbsp;</td>
<td class="color_td" style="background:#FFFFCC" onmouseover="setColor('#FFFFCC')">&nbsp;</td>
<td class="color_td" style="background:#E5FFCC" onmouseover="setColor('#E5FFCC')">&nbsp;</td>
<td class="color_td" style="background:#CCFFCC" onmouseover="setColor('#CCFFCC')">&nbsp;</td>
<td class="color_td" style="background:#CCFFE5" onmouseover="setColor('#CCFFE5')">&nbsp;</td>
<td class="color_td" style="background:#CCFFFF" onmouseover="setColor('#CCFFFF')">&nbsp;</td>
<td class="color_td" style="background:#CCE5FF" onmouseover="setColor('#CCE5FF')">&nbsp;</td>
<td class="color_td" style="background:#CCCCFF" onmouseover="setColor('#CCCCFF')">&nbsp;</td>
<td class="color_td" style="background:#E5CCFF" onmouseover="setColor('#E5CCFF')">&nbsp;</td>
<td class="color_td" style="background:#FFCCFF" onmouseover="setColor('#FFCCFF')">&nbsp;</td>
<td class="color_td" style="background:#FFCCE5" onmouseover="setColor('#FFCCE5')">&nbsp;</td>
<td class="color_td" style="background:#FFFFFF" onmouseover="setColor('#FFFFFF')">&nbsp;</td>
</tr>
</tbody></table>

RGB Color Tuple: <input type="text" id="RGBTupleField" />


## Filling in Shapes

The turtle can draw the outline of a shape and then fill it in with color using the fill functions. The filling process starts when the begin_color() function is called. The turtle can move around as normal. When the end_fill() function is called, the shape the turtle was drawing will be filled with the fill color. The fill color is separate from the pen color.

```python
from turtle import *

fillcolor('purple')
pensize(10)
pencolor('black')
forward(100)

begin_fill()
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
end_fill()
```

[<img src="fill.png" class="screenshot" />](fill.png)

### fillcolor(), fillcolor(*color*), fillcolor((*red*, *green*, *blue*)), fillcolor(*red*, *green*, *blue*)

The fillcolor() function sets the color of the filled in shape when end_fill() is called. The fillcolor() function can be passed a string of the color, such as 'red' or 'black'. Or, the fillcolor() function can be passed an "RGB color tuple" (see the [Color](#color) section).

### begin_fill()

The begin_fill() starts recording the moves that will be the outline of the filled-in shape. The filled-in shape will not be drawn until end_fill() is called.

### end_fill()

The end_fill() function will stop recording the moves for the filled-in shape and draw the shape.


## Stamping

### stamp()

```python
from turtle import *

penup()

for i in range(30, -1, -1):
    stamp()
    left(i)
    forward(20)
```

[<img src="stamp.png" class="screenshot" />](stamp.png)

### clearstamp()

### clearstamps()



## Animation

### tracer()



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

```python
from turtle import *

def up():
    setheading(90)
    forward(100)

def down():
    setheading(270)
    forward(100)

def left():
    setheading(180)
    forward(100)

def right():
    setheading(0)
    forward(100)

listen()

onkey(up, 'Up')
onkey(down, 'Down')
onkey(left, 'Left')
onkey(right, 'Right')

onkey(up, 'w')
onkey(down, 's')
onkey(left, 'a')
onkey(right, 'd')
```

[<img src="onkey.png" class="screenshot" />](onkey.png)

up, right, down, down, left, left, up


### onkeypress()

```python
from turtle import *

def blue_screen():
    bgcolor(0.7, 1.0, 1.0)

def white_screen():
    bgcolor(1.0, 1.0, 1.0)

listen()
onkeypress(blue_screen, 'space')
onkey(white_screen, 'space')
```

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