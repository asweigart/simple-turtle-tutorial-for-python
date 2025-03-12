from turtle import *

# Set up some constants for slider positions:
RED_X = -200
GREEN_X = 0
BLUE_X = 200
TOP = 200
BOTTOM = -200
SLIDER_LENGTH = abs(TOP - BOTTOM)
CLICK_RANGE = 20
TEXT_OFFSET = -75
COLOR_BOXES = ((0,0,0), (128,128,128), (128,0,0), (128,128,0), (0,128,0), (0,128,128), (0,0,128), (128,0,128), (128,128,64), (0,64,64), (0,128,255), (0,64,128), (128,0,255), (128,64,0),
    (255,255,255), (192,192,192), (255,0,0), (255,255,0), (0,255,0), (0,255,255), (0,0,255), (255,0,255), (255,255,128), (0,255,128), (128,255,255), (128,128,255), (255,0,128), (255,128,64))
COLOR_BOX_SIZE = 30
COLOR_BOX_TOP = 280
COLOR_BOX_LEFT = -240
COLOR_BOX_GAP = 5

# Set up global variables:
red_setting = 0.5
green_setting = 0.5
blue_setting = 0.5
bgcolor((red_setting, green_setting, blue_setting))
color_box_values = []

# Draw slider lines:
tracer(1000, 0)
hideturtle()
pensize(6)
setheading(270)
for x in (RED_X, 0, BLUE_X):
    penup()
    goto(x, TOP)
    pendown()
    forward(SLIDER_LENGTH)

# Draw color boxes:
colormode(255)
pensize(1)
for i, color in enumerate(COLOR_BOXES):
    if i < 14:
        x = COLOR_BOX_LEFT + (i * COLOR_BOX_SIZE) + (i * COLOR_BOX_GAP)
        y = COLOR_BOX_TOP  # Top row of the two rows.
    else:
        x = COLOR_BOX_LEFT + ((i-14) * COLOR_BOX_SIZE) + ((i-14) * COLOR_BOX_GAP)
        y = COLOR_BOX_TOP - COLOR_BOX_GAP - COLOR_BOX_SIZE  # Bottom row of the two rows.
    color_box_values.append((x,y))

    penup()
    goto(x, y)
    setheading(0)
    pendown()
    fillcolor(color)
    begin_fill()
    for j in range(4):
        forward(COLOR_BOX_SIZE)
        right(90)
    end_fill()
colormode(1)

# Create new turtle cursors for the square slider handles:
red_cursor = Turtle()
green_cursor = Turtle()
blue_cursor = Turtle()
for cursor, color, x in ((red_cursor, 'red', RED_X), (green_cursor, 'green', GREEN_X), (blue_cursor, 'blue', BLUE_X)):
    cursor.speed('fastest')
    cursor.shape('square')
    cursor.fillcolor(color)
    cursor.penup()
    cursor.goto(x, 0)

# Create a new turtle cursor for the text:
rw = Turtle() 
gw = Turtle() 
bw = Turtle() 
for t in (rw, gw, bw):
    t.hideturtle()
    t.penup()
    t.pencolor('black')



def handle_click(x, y):
    #print('click', x, y)
    # Check if the click is on a color box:
    

    # Check if the click is on a slider:
    if y > TOP or y < BOTTOM:
        return  # Outside of range, so do nothing.
    elif x >= RED_X - CLICK_RANGE and x <= RED_X + CLICK_RANGE:
        # Only the drag function if the click happened off of the turtle cursor:
        if y > red_cursor.ycor() + 10 or y < red_cursor.ycor() - 10:
            handle_red_drag(x, y)
    elif x >= GREEN_X - CLICK_RANGE and x <= GREEN_X + CLICK_RANGE:
        # Only the drag function if the click happened off of the turtle cursor:
        if y > green_cursor.ycor() + 10 or y < green_cursor.ycor() - 10:
            handle_green_drag(x, y)
    elif x >= BLUE_X - CLICK_RANGE and x <= BLUE_X + CLICK_RANGE:
        # Only the drag function if the click happened off of the turtle cursor:
        if y > blue_cursor.ycor() + 10 or y < blue_cursor.ycor() - 10:
            handle_blue_drag(x, y)


def write_rgb_values():
    #print((red_setting, green_setting, blue_setting))

    if (red_setting + green_setting + blue_setting) / 3 < 0.5:
        rw.pencolor('white')
        gw.pencolor('white')
        bw.pencolor('white')
    else:
        rw.pencolor('black')
        gw.pencolor('black')
        bw.pencolor('black')

    red_text = str(round(red_setting, 2)).ljust(4, '0') + '   ' + str(round(red_setting * 255))
    rw.clear()
    rw.goto(RED_X + TEXT_OFFSET, BOTTOM - 50)
    rw.write(red_text, font=('Arial', 24, 'normal'))

    green_text = str(round(green_setting, 2)).ljust(4, '0') + '   ' + str(round(green_setting * 255))
    gw.clear()
    gw.goto(GREEN_X + TEXT_OFFSET, BOTTOM - 50)
    gw.write(green_text, font=('Arial', 24, 'normal'))

    blue_text = str(round(blue_setting, 2)).ljust(4, '0') + '   ' + str(round(blue_setting * 255))
    bw.clear()
    bw.goto(BLUE_X + TEXT_OFFSET, BOTTOM - 50)
    bw.write(blue_text, font=('Arial', 24, 'normal'))

    update()


def handle_red_drag(x, y):
    global red_setting
    print('red drag', x, y)

    if y > TOP:
        red_setting = 1.0
        red_cursor.sety(TOP)
    elif y < BOTTOM:
        red_setting = 0.0
        red_cursor.sety(BOTTOM)
    else:
        red_setting = abs(y - BOTTOM) / SLIDER_LENGTH
        red_cursor.sety(y)

    #print('red drag', x, y, red_setting)
    bgcolor((red_setting, green_setting, blue_setting))
    write_rgb_values()


def handle_green_drag(x, y):
    global green_setting
    print('green drag', x, y)

    if y > TOP:
        green_setting = 1.0
        green_cursor.sety(TOP)
    elif y < BOTTOM:
        green_setting = 0.0
        green_cursor.sety(BOTTOM)
    else:
        green_setting = abs(y - BOTTOM) / SLIDER_LENGTH
        green_cursor.sety(y)

    #print('green drag', x, y, green_setting)
    bgcolor((red_setting, green_setting, blue_setting))
    write_rgb_values()
    

def handle_blue_drag(x, y):
    global blue_setting
    print('blue drag', x, y)

    if y > TOP:
        blue_setting = 1.0
        blue_cursor.sety(TOP)
    elif y < BOTTOM:
        blue_setting = 0.0
        blue_cursor.sety(BOTTOM)
    else:
        blue_setting = abs(y - BOTTOM) / SLIDER_LENGTH
        blue_cursor.sety(y)

    #print('blue drag', x, y, blue_setting)
    bgcolor((red_setting, green_setting, blue_setting))
    write_rgb_values()
    

getscreen().onclick(handle_click)
red_cursor.ondrag(handle_red_drag)
green_cursor.ondrag(handle_green_drag)
blue_cursor.ondrag(handle_blue_drag)
#ontimer(write_rgb_values)
write_rgb_values()

update()
done()
