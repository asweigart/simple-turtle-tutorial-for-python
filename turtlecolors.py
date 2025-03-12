from turtle import *

# Set up some constants for slider positions:
RED_X = -200
GREEN_X = 0
BLUE_X = 200
TOP = 200
BOTTOM = -200
SLIDER_LENGTH = abs(TOP - BOTTOM)
CLICK_RANGE = 40
TEXT_X_OFFSET = -75
TEXT_Y = BOTTOM - 60
COLOR_BOXES = ((0,0,0), (128,128,128), (128,0,0), (128,128,0), (0,128,0), (0,128,128), (0,0,128), (128,0,128), (128,128,64), (0,64,64), (0,128,255), (0,64,128), (128,0,255), (128,64,0),
    (255,255,255), (192,192,192), (255,0,0), (255,255,0), (0,255,0), (0,255,255), (0,0,255), (255,0,255), (255,255,128), (0,255,128), (128,255,255), (128,128,255), (255,0,128), (255,128,64))
COLOR_BOX_SIZE = 30
COLOR_BOX_TOP = 320
COLOR_BOX_LEFT = -240
COLOR_BOX_GAP = 5

# Set up global variables:
red_setting = 0.5
green_setting = 0.5
blue_setting = 0.5
bgcolor((red_setting, green_setting, blue_setting))
color_box_positions = []
red_cursor = Turtle()
green_cursor = Turtle()
blue_cursor = Turtle()
rw = Turtle() 
gw = Turtle() 
bw = Turtle() 


def print_color_values():
    # Note: I could have hard-coded all these color values, but I'd
    # to know if any of these names become invalid for turtle.py.

    canvas = getcanvas()

    # Convert color name to RGB tuple:
    for color_name in ('aliceblue','antiquewhite','antiquewhite1','antiquewhite2','antiquewhite3','antiquewhite4','aqua','aquamarine1','aquamarine2','aquamarine3','aquamarine4','azure','azure1','azure2','azure3','azure4','beige','bisque1','bisque2','bisque3','bisque4','black','blanchedalmond','blue','blue2','blue3','blue4','blueviolet','brown','brown1','brown2','brown3','brown4','burlywood','burlywood1','burlywood2','burlywood3','burlywood4','cadetblue','cadetblue1','cadetblue2','cadetblue3','cadetblue4','chartreuse','chartreuse1','chartreuse2','chartreuse3','chartreuse4','chocolate','chocolate1','chocolate2','chocolate3','chocolate4','coral','coral1','coral2','coral3','coral4','cornflowerblue','cornsilk','cornsilk1','cornsilk2','cornsilk3','cornsilk4','crimson','cyan','cyan2','cyan3','cyan4','darkgoldenrod','darkgoldenrod1','darkgoldenrod2','darkgoldenrod3','darkgoldenrod4','darkgray','darkgreen','darkkhaki','darkolivegreen','darkolivegreen1','darkolivegreen2','darkolivegreen3','darkolivegreen4','darkorange','darkorange1','darkorange2','darkorange3','darkorange4','darkorchid','darkorchid1','darkorchid2','darkorchid3','darkorchid4','darksalmon','darkseagreen','darkseagreen1','darkseagreen2','darkseagreen3','darkseagreen4','darkslateblue','darkslategray','darkslategray1','darkslategray2','darkslategray3','darkslategray4','darkturquoise','darkviolet','deeppink1','deeppink2','deeppink3','deeppink4','deepskyblue','deepskyblue1','deepskyblue2','deepskyblue3','deepskyblue4','dimgray','dodgerblue1','dodgerblue2','dodgerblue3','dodgerblue4','firebrick','firebrick1','firebrick2','firebrick3','firebrick4','floralwhite','forestgreen','gainsboro','ghostwhite','gold1','gold2','gold3','gold4','goldenrod','goldenrod1','goldenrod2','goldenrod3','goldenrod4','gray','gray1','gray10','gray11','gray12','gray13','gray14','gray15','gray16','gray17','gray18','gray19','gray2','gray20','gray21','gray22','gray23','gray24','gray25','gray26','gray27','gray28','gray29','gray3','gray30','gray31','gray32','gray33','gray34','gray35','gray36','gray37','gray38','gray39','gray4','gray40','gray42','gray43','gray44','gray45','gray46','gray47','gray48','gray49','gray5','gray50','gray51','gray52','gray53','gray54','gray55','gray56','gray57','gray58','gray59','gray6','gray60','gray61','gray62','gray63','gray64','gray65','gray66','gray67','gray68','gray69','gray7','gray70','gray71','gray72','gray73','gray74','gray75','gray76','gray77','gray78','gray79','gray8','gray80','gray81','gray82','gray83','gray84','gray85','gray86','gray87','gray88','gray89','gray9','gray90','gray91','gray92','gray93','gray94','gray95','gray97','gray98','gray99','green','green1','green2','green3','green4','greenyellow','honeydew1','honeydew2','honeydew3','honeydew4','hotpink','hotpink1','hotpink2','hotpink3','hotpink4','indianred','indianred1','indianred2','indianred3','indianred4','indigo','ivory1','ivory2','ivory3','ivory4','khaki','khaki1','khaki2','khaki3','khaki4','lavender','lavenderblush1','lavenderblush2','lavenderblush3','lavenderblush4','lawngreen','lemonchiffon1','lemonchiffon2','lemonchiffon3','lemonchiffon4','lightblue','lightblue1','lightblue2','lightblue3','lightblue4','lightcoral','lightcyan1','lightcyan2','lightcyan3','lightcyan4','lightgoldenrod1','lightgoldenrod2','lightgoldenrod3','lightgoldenrod4','lightgoldenrodyellow','lightgrey','lightpink','lightpink1','lightpink2','lightpink3','lightpink4','lightsalmon1','lightsalmon2','lightsalmon3','lightsalmon4','lightseagreen','lightskyblue','lightskyblue1','lightskyblue2','lightskyblue3','lightskyblue4','lightslateblue','lightslategray','lightsteelblue','lightsteelblue1','lightsteelblue2','lightsteelblue3','lightsteelblue4','lightyellow1','lightyellow2','lightyellow3','lightyellow4','limegreen','linen','magenta','magenta2','magenta3','magenta4','maroon','maroon1','maroon2','maroon3','maroon4','mediumorchid','mediumorchid1','mediumorchid2','mediumorchid3','mediumorchid4','mediumpurple','mediumpurple1','mediumpurple2','mediumpurple3','mediumpurple4','mediumseagreen','mediumslateblue','mediumspringgreen','mediumturquoise','mediumvioletred','midnightblue','mintcream','mistyrose1','mistyrose2','mistyrose3','mistyrose4','moccasin','navajowhite1','navajowhite2','navajowhite3','navajowhite4','navy','oldlace','olive','olivedrab','olivedrab1','olivedrab2','olivedrab3','olivedrab4','orange','orange1','orange2','orange3','orange4','orangered1','orangered2','orangered3','orangered4','orchid','orchid1','orchid2','orchid3','orchid4','palegoldenrod','palegreen','palegreen1','palegreen2','palegreen3','palegreen4','paleturquoise1','paleturquoise2','paleturquoise3','paleturquoise4','palevioletred','palevioletred1','palevioletred2','palevioletred3','palevioletred4','papayawhip','peachpuff1','peachpuff2','peachpuff3','peachpuff4','pink','pink1','pink2','pink3','pink4','plum','plum1','plum2','plum3','plum4','powderblue','purple','purple1','purple2','purple3','purple4','red1','red2','red3','red4','rosybrown','rosybrown1','rosybrown2','rosybrown3','rosybrown4','royalblue','royalblue1','royalblue2','royalblue3','royalblue4','salmon','salmon1','salmon2','salmon3','salmon4','sandybrown','seagreen1','seagreen2','seagreen3','seagreen4','seashell1','seashell2','seashell3','seashell4','sienna','sienna1','sienna2','sienna3','sienna4','silver','skyblue','skyblue1','skyblue2','skyblue3','skyblue4','slateblue','slateblue1','slateblue2','slateblue3','slateblue4','slategray','slategray1','slategray2','slategray3','slategray4','snow1','snow2','snow3','snow4','springgreen','springgreen1','springgreen2','springgreen3','steelblue','steelblue1','steelblue2','steelblue3','steelblue4','tan','tan1','tan2','tan3','tan4','teal','thistle','thistle1','thistle2','thistle3','thistle4','tomato1','tomato2','tomato3','tomato4','turquoise','turquoise1','turquoise2','turquoise3','turquoise4','violet','violetred','violetred1','violetred2','violetred3','violetred4','wheat','wheat1','wheat2','wheat3','wheat4','white','whitesmoke','yellow1','yellow2','yellow3','yellow4'):
        rgb_16bit = canvas.winfo_rgb(color_name)  # e.g. returns (65535, 0, 0) for 'red'.
        rgb_255 = tuple(c // 256 for c in rgb_16bit)  # Scale down to 8-bit.
        rgb_1 = tuple([round(n / 255, 2) for n in rgb_255])
        rgb_hex = '#' + ''.join([hex(n)[2:].rjust(2, '0').upper() for n in rgb_255])

        # Separated by dashes for easy double-click highlighting (and not CSV because tuples contain commas):
        print(color_name, rgb_255, rgb_1, rgb_hex, sep='-')


def handle_click(x, y):
    global red_setting, green_setting, blue_setting

    #print('click', x, y)
    
    # Check if the click is on a color box:
    for i, (boxx, boxy) in enumerate(color_box_positions):
        if (boxx <= x <= (boxx + COLOR_BOX_SIZE)) and (boxy >= y >= (boxy - COLOR_BOX_SIZE)):
            #print('color box clicked', i)
            red_setting, green_setting, blue_setting = COLOR_BOXES[i]

            # Adjust for colormode 1 (the values in COLOR_BOXES are in colormode 255):
            red_setting /= 255
            green_setting /= 255
            blue_setting /= 255

            # Move sliders into correct position:
            red_cursor.sety(  BOTTOM + (SLIDER_LENGTH * red_setting))
            green_cursor.sety(BOTTOM + (SLIDER_LENGTH * green_setting))
            blue_cursor.sety( BOTTOM + (SLIDER_LENGTH * blue_setting))

            # Update background color and text:
            bgcolor((red_setting, green_setting, blue_setting))
            write_rgb_values()



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


def get_color_values_text(setting):
    spacer = '  '
    setting255 = round(setting * 255)

    return str(round(setting, 2)).ljust(4, '0') + spacer + \
        str(setting255) + spacer + \
        '#' + hex(setting255)[2:].rjust(2, '0').upper()

def write_rgb_values():
    #print((red_setting, green_setting, blue_setting))

    # Make text white when background is dark, and black when background is light:
    if (red_setting + green_setting + blue_setting) / 3 < 0.5:
        rw.pencolor('white')
        gw.pencolor('white')
        bw.pencolor('white')
    else:
        rw.pencolor('black')
        gw.pencolor('black')
        bw.pencolor('black')

    for cursor, x, setting in ((rw, RED_X, red_setting), (gw, GREEN_X, green_setting), (bw, BLUE_X, blue_setting)):
        cursor.clear()
        cursor.goto(x + TEXT_X_OFFSET, TEXT_Y)
        cursor.write(get_color_values_text(setting), font=('Arial', 18, 'normal'))

    update()


def handle_red_drag(x, y):
    global red_setting
    #print('red drag', x, y)

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
    #print('green drag', x, y)

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
    #print('blue drag', x, y)

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
    

def main():
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
        color_box_positions.append((x,y))

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

    # Setup turtle cursors for the square slider handles:
    for cursor, color, x in ((red_cursor, 'red', RED_X), (green_cursor, 'green', GREEN_X), (blue_cursor, 'blue', BLUE_X)):
        cursor.resizemode('auto')
        cursor.pensize(10)
        cursor.shape('square')
        cursor.fillcolor(color)
        cursor.penup()
        cursor.goto(x, 0)

    # Setup turtle cursors for the text:
    for t in (rw, gw, bw):
        t.hideturtle()
        t.penup()
        t.pencolor('black')


    # Print all color names and their values to stdio for easy copy/pasting:
    print_color_values()

    getscreen().onclick(handle_click)
    red_cursor.ondrag(handle_red_drag)
    green_cursor.ondrag(handle_green_drag)
    blue_cursor.ondrag(handle_blue_drag)
    #ontimer(write_rgb_values)
    write_rgb_values()

    update()
    done()



if __name__ == '__main__':
    main()
