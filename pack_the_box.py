""" Pack the box.

container: The container can either be a square or a rectangle.
Parameters to define the container are: square = true or false, h_size, v_size

item: The item can be a square, a rectangle, or a circle.
Parameters to define the item are: shape = 0, 1, 2; h_size, v_size, or radius if circle

Possible enhancements:
1). Implement a faster drawing package.
2). Extend to 3D.
3). Make web app with sleek user interface.

"""

import sys

from random import random, randrange
from math import sqrt, pi, ceil

from classes import Container, Shape

import turtle


def create_container():
    """Asks user for dimensions and returns instance of Container class."""

    prompt_height = "What is the height of your container? default:400 range:100-700 >>> "
    height = collect_valid_input(prompt_height,400,[100,700])

    prompt_width = "What is the width of your container? default:400 range:100-1000 >>> "
    width = collect_valid_input(prompt_width,400,[100,1000])

    container = Container(height, width)
    return container


def create_shape():
    """Asks user for parameters to create instance of Shape class, which will be the item to keep adding to container."""

    # shape_key = gen_random_shape()
    prompt_shape = "Enter shape type: 0 FOR RECT or 1 FOR CIRCLE. default:0 >>> "
    shape_key = collect_valid_input(prompt_shape,0,[0,1])

    if shape_key == 0:
        prompt_h = "Enter height of RECT or SQUARE to be inserted.  default:30,30 range:1-50 >>> "
        prompt_w = "Enter width of RECT or SQUARE to be inserted.  default:30,30 range:1-50 >>> "
        height,width = collect_valid_input(prompt_h,30,[1,50]), collect_valid_input(prompt_w,30,[1,50])
        shape = Shape(height,width)

    elif shape_key == 1:
        prompt_r = "Enter radius of CIRCLE to be inserted. default:15 range:1-25 >>> "
        radius = collect_valid_input(prompt_r,15,[1,25])
        shape = Shape(radius)

    return shape


def pack_item(container,shape,limits):

    x,y = gen_random_coord(limits)

    if does_not_overlap(container,shape,x,y):
        container.add_items(shape,x,y)
        return True

    return False


def keep_packing(container,shape,limits):
    """Attempts to fit next item."""

    drawn = 0
    not_drawn = 0

    consec_drawn = 1
    consec_not_drawn = 1
    max_consec_drawn = 0
    max_consec_not_drawn = 0

    while True:
        if (pack_item(container,shape,limits)):
            drawn += 1
            consec_drawn += 1
            if consec_drawn > max_consec_drawn:
                max_consec_drawn = consec_drawn
            if consec_not_drawn > max_consec_not_drawn:
                max_consec_not_drawn = consec_not_drawn
            consec_not_drawn = 1
        else:
            not_drawn += 1
            consec_not_drawn += 1
            consec_drawn = 1

            if consec_not_drawn == LOOP_LIMIT:
                tracker(drawn,not_drawn,consec_not_drawn,max_consec_drawn,max_consec_not_drawn)
                break


### TURTLE HELPER FUNCTIONS ###

def set_turtle(WIDTH,HEIGHT,STARTX,STARTY,COLOR,SPEED):
    """Defines turtle interface."""

    screen = turtle.getscreen()
    screen.title("Pack the box!")
    screen.bgcolor(COLOR)
    screen.setup(width=WIDTH, height=HEIGHT, startx=STARTX, starty=STARTY)
    turtle.speed(SPEED)
    print("Ready to draw...")


def draw_container(container):
    """Turtle draws container instance."""

    turtle.shape('classic')
    turtle.color('', '')
    turtle.pensize(3)
    turtle.begin_fill()
    turtle.setheading(0)
    turtle.setpos(int(-container.width/2), int(container.height/2))
    turtle.color('white', 'yellow')
    turtle.forward(int(container.width))
    turtle.right(90)
    turtle.forward(int(container.height))
    turtle.right(90)
    turtle.forward(int(container.width))
    turtle.right(90)
    turtle.forward(int(container.height))
    turtle.color('yellow', '')
    turtle.fillcolor('#DDDDDD')
    turtle.end_fill()


def label_coordinates(x,y):
    """Uses Turtle to label coordinates of center."""

    turtle.color('', '')

    turtle.setpos(x,y)
    position = '('+str(x)+', '+str(y)+')'
    turtle.pencolor('black')
    turtle.write(position)


def draw_rect(shape,x,y):
    """Uses Turtle to draw a rectangle."""

    turtle.shape('classic')
    turtle.color('', '')
    turtle.pensize(1)
    turtle.begin_fill()
    turtle.setheading(0)
    turtle.setpos(int(x-shape.width/2), int(y+shape.height/2))
    turtle.color('#444444', 'black')
    turtle.forward(shape.width)
    turtle.right(90)
    turtle.forward(shape.height)
    turtle.right(90)
    turtle.forward(shape.width)
    turtle.right(90)
    turtle.forward(shape.height)
    turtle.color('black', 'white')
    turtle.fillcolor('violet')
    turtle.end_fill()


def draw_circle(shape,x,y):
    """Uses Turtle to draw a circle."""

    turtle.shape('classic')
    turtle.color('', '')
    turtle.pensize(1)
    turtle.begin_fill()
    turtle.setpos(int(x+shape.radius), int(y))
    turtle.color('red', 'black')
    turtle.circle(int(shape.radius))
    turtle.color('black', '')
    turtle.fillcolor('white')
    turtle.end_fill()


def draw_sequence(container,shape):

    turtle.clear()

    draw_container(container)
    print("Now DRAWING !!")

    for item in container.items:
        shape = item['item']
        coordinates = item['coordinates']['x'],item['coordinates']['y']
        if vars(shape)['type'] == 'circle':
            draw_circle(shape,coordinates[0],coordinates[1])
        elif vars(shape)['type'] == 'rectangle':
            draw_rect(shape,coordinates[0],coordinates[1])
        label_coordinates(coordinates[0],coordinates[1])

    print("Drawing complete.")


### HELPER FUNCTIONS ###

def collect_valid_input(prompt,default,value_range):
    """Collects valid input from user, given a prompt."""

    while True:
        try:
            value = int(input(prompt) or default)
        except ValueError:
            print("Invalid entry.")
            continue

        if value < value_range[0] or value > value_range[1]:
            print("Please enter a number between " + str(value_range[0]) + " and " + str(value_range[1]) + ".")
            continue
        else:
            break

    return value


def gen_random_shape():
    """If the program wants to randomize type of shape."""

    shape_key = randrange(0,2,1)
    return shape_key


def gen_random_coord(limits):
    """Program generates random coordinate at which to pack item."""

    scale_x = random() - 0.5
    scale_y = random() - 0.5

    if scale_x <= 0:
        x = round(-limits[3] * scale_x, 2)
    elif scale_x > 0:
        x = round(limits[2] * scale_x, 2)

    if scale_y <= 0:
        y = round(-limits[1] * scale_y, 2)
    elif scale_y > 0:
        y = round(limits[0] * scale_y, 2)

    return x,y


def pad_container(container,shape):
    """Pads container bounds according to size of item."""

    if vars(shape)['type'] == 'circle':
        padding = shape.radius*2, shape.radius*2, shape.radius*2, shape.radius*2
    elif vars(shape)['type'] == 'rectangle':
        padding = shape.height, shape.height, shape.width, shape.width

    top_limit = container.height - padding[0]
    bottom_limit = -container.height + padding[1]
    right_limit = container.width - padding[2]
    left_limit = -container.width + padding[3]

    return top_limit, bottom_limit, right_limit, left_limit


def does_not_overlap(container,shape,x,y):
    """Returns True if no overlap with existing items, called every time before item is inserted."""

    if vars(shape)['type'] == 'circle':
        for item in container.items:
            center = item.get('coordinates')
            if (shape.radius*2) < sqrt(((x - center['x'])**2) + ((y - center['y'])**2)):
                # print("true: x,y: ", x, y, center['x'], center['y'])
                continue
            else:
                # print("false")
                return False
        return True

    elif vars(shape)['type'] == 'rectangle':
        for item in container.items:
            center = item.get('coordinates')
            if y < (center['y']-shape.height) or y > (center['y']+shape.height):
                # print("true: y: ", y, center['y'])
                continue
            elif x < (center['x']-shape.width) or x > (center['x']+shape.width):
                # print("true: x: ", x, center['x'])
                continue
            else:
                # print("false")
                return False
        return True


### EXTRACT DATA ###

def calculate_container_area(container):
    return container.height * container.width


def calculate_shape_area(shape):
    if vars(shape)['type'] == 'circle':
        return (shape.radius**2) * pi
    elif vars(shape)['type'] == 'rectangle':
        return shape.height * shape.width


def calculate_efficiency(container,shape):
    container_area = calculate_container_area(container)
    shape_area = calculate_shape_area(shape)
    efficiency = shape_area * len(container.items) / container_area
    return ceil(efficiency * 100 * 100) / 100.


def tracker(drawn,
            not_drawn,
            consec_not_drawn,
            max_consec_drawn,
            max_consec_not_drawn):
    """Tracks data."""

    print("Total items drawn: " + str(drawn))
    print("Total items not drawn: " + str(not_drawn))
    print("Max consecutive items drawn: " + str(max_consec_drawn))
    print("Consecutive items not drawn (max LOOP_LIMIT " + str(LOOP_LIMIT) + "): " + str(consec_not_drawn))
    print("Max consecutive items not drawn (previous to max being reached): " + str(max_consec_not_drawn))


### PRIMARY FUNCTION TO RUN PROGRAM ###

def pack_the_box(LOOP_LIMIT):
    """Initializes container and shape, as well as limits of container based on shape."""

    # setup
    container = create_container()
    shape = create_shape()
    print("Container: ", vars(container), "Is a square?", container.is_square())
    print("Shape variables: ", vars(shape))

    container.items = []  # reset container if program has already been run
    dimension_limits = pad_container(container,shape)

    # pack the box
    keep_packing(container,shape,dimension_limits)

    # calculate area efficiency score
    efficiency = calculate_efficiency(container,shape)
    print("Packing efficiency: " + str(efficiency) + "%")

    # visualize
    draw_sequence(container,shape)

    try_again = input("Would you like to try again? (Y/N) >>> ")
    if try_again == 'Y':
        pack_the_box(LOOP_LIMIT)
    elif try_again == 'N':
        exit()


#############################################

if __name__ == "__main__":
    # import doctest
    # result = doctest.testmod()
    # if not result.failed:
    #     print("ALL TESTS PASSED. GOOD WORK!")

    set_turtle(WIDTH=1.0,HEIGHT=1.0,STARTX=0,STARTY=0,COLOR="#EFEFEF",SPEED=0)

    LOOP_LIMIT = 100000
    pack_the_box(LOOP_LIMIT)


# TODO add way for user to reset and try another shape, size container without exiting the program.
# TODO record results.


# def keep_packing():

#     attempts = 0

#     while True:
#         pack_item()
#         attempts += 1
#         if attempts >= 1000 + len(container.items):
#             print (attempts)
#             break
