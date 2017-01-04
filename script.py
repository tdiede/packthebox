""" Pack the box.

container: The container can either be a square or a rectangle.
Parameters to define the container are: square = true or false, h_size, v_size

item: The item can be a square, a rectangle, or a circle.
Parameters to define the item are: shape = 0, 1, 2; h_size, v_size, or radius if circle
"""


from random import random, randrange
from math import sqrt, pi

import turtle

from classes import Container, Shape


screen = turtle.getscreen()
screen.title("Pack the box!")
screen.bgcolor("#80A080")
screen.setup(width=0.5, height=0.8, startx=50, starty=None)

turtle.speed(0)


def create_container():

    height = input("What is the height of your container? default:600 >>>")
    width = input("What is the width of your container? default:500 >>>")
    if height and width:
        container = Container(height, width)
    container = Container()

    turtle.shape('classic')
    turtle.color('', '')
    turtle.begin_fill()
    turtle.setpos(-int(container.width)/2, int(container.height)/2)
    turtle.color('red', 'yellow')
    turtle.forward(int(container.width))
    turtle.right(90)
    turtle.forward(int(container.height))
    turtle.right(90)
    turtle.forward(int(container.width))
    turtle.right(90)
    turtle.forward(int(container.height))
    turtle.color('yellow', 'white')
    turtle.end_fill()

    return container


def gen_random_item():
    """Generates a random type of next item to keep adding to container."""

    shape_key = gen_random_shape()

    if shape_key == 0:
        dimensions = input("What is the desired height/width of your rectangle? default:40,90 >>>") or '40,90'
        height, width = dimensions.split(',')
        shape = Shape(int(height), int(width))
        # draw_rect(shape)

    elif shape_key == 1:
        radius = input("What is the desired radius of your circle? default:40 >>>") or '40'
        shape = Shape(int(radius))
        # draw_circle(shape)

    return shape


def keep_packing():

    attempts = 0

    while True:
        pack_item()
        attempts += 1
        if attempts >= 1000 + len(container.items):
            print (attempts)
            break


def pack_item():

    x,y = gen_random_coord()

    while does_not_overlap(x,y):

        label_coordinates(x,y)
        if vars(shape)['type'] == 'circle':
            draw_circle(shape,x,y)
        elif vars(shape)['type'] == 'rectangle':
            draw_rect(shape,x,y)

        container.add_items(shape,x,y)
        print (container.items)

        efficiency = calculate_efficiency()
        print (efficiency)

        x,y = gen_random_coord()


def does_not_overlap(x,y):
    """Returns True if no overlap with existing items."""

    if vars(shape)['type'] == 'circle':
        for item in container.items:
            center = item.get('coordinates')
            if (shape.radius*2) < sqrt(((x - center['x'])**2) + ((y - center['y'])**2)):
                print ("true: x,y: ", x, y, center['x'], center['y'])
                continue
            else:
                print ("false")
                return False
        return True
    elif vars(shape)['type'] == 'rectangle':
        for item in container.items:
            center = item.get('coordinates')
            if y < (center['y']-shape.height) or y > (center['y']+shape.height):
                print ("true: y: ", y, center['y'])
                continue
            elif x < (center['x']-shape.width) or x > (center['x']+shape.width):
                print ("true: x: ", x, center['x'])
                continue
            else:
                print ("false")
                return False
        return True


### TURTLE HELPER FUNCTIONS ###

def label_coordinates(x,y):
    """Uses Turtle to label coordinates of center."""

    turtle.color('', '')

    turtle.setpos(x,y)
    position = '('+str(x)+', '+str(y)+')'
    turtle.color('black', 'blue')
    turtle.write(position)


def draw_rect(shape,x,y):
    """Uses Turtle to draw a rectangle."""

    turtle.shape('classic')
    turtle.color('', '')
    turtle.begin_fill()
    turtle.setheading(0)
    turtle.setpos(x-shape.width/2, y+shape.height/2)
    turtle.color('blue', 'black')
    turtle.forward(shape.width)
    turtle.right(90)
    turtle.forward(shape.height)
    turtle.right(90)
    turtle.forward(shape.width)
    turtle.right(90)
    turtle.forward(shape.height)
    turtle.color('black', '')
    turtle.end_fill()


def draw_circle(shape,x,y):
    """Uses Turtle to draw a circle."""

    turtle.shape('classic')
    turtle.color('', '')
    turtle.begin_fill()
    turtle.setpos(x+shape.radius, y)
    turtle.color('black', 'red')
    turtle.circle(shape.radius)
    turtle.color('black', '')
    turtle.end_fill()


### RANDOM HELPER FUNCTIONS ###

def pad_container():
    """Pads container bounds according to size of item."""

    if vars(shape)['type'] == 'circle':
        return shape.radius*2, shape.radius*2, shape.radius*2, shape.radius*2
    elif vars(shape)['type'] == 'rectangle':
        return shape.height, shape.width, shape.height, shape.width


def gen_random_coord():

    padding = pad_container()

    top_limit = container.height - padding[0]
    right_limit = container.width - padding[1]
    bottom_limit = -container.height + padding[2]
    left_limit = -container.width + padding[3]

    scale_x = random() - 0.5
    scale_y = random() - 0.5

    if scale_x <= 0:
        x = round(-left_limit * scale_x, 2)
    elif scale_x > 0:
        x = round(right_limit * scale_x, 2)

    if scale_y <= 0:
        y = round(-bottom_limit * scale_y, 2)
    elif scale_y > 0:
        y = round(top_limit * scale_y, 2)

    print (x,y)
    return x,y


def gen_random_shape():

    shape_key = randrange(0,2,1)
    return shape_key


### EXTRACT DATA ###

def calculate_efficiency():

    efficiency = shape_area * len(container.items) / container_area
    return efficiency


#############################################

if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    if not result.failed:
        print ("ALL TESTS PASSED. GOOD WORK!")

    container = create_container()
    shape = gen_random_item()
    print (container.width, container.height, container.is_square())
    print (vars(shape))

    container_area = container.height * container.width
    if vars(shape)['type'] == 'circle':
        shape_area = (shape.radius**2) * pi
    elif vars(shape)['type'] == 'rectangle':
        shape_area = shape.height * shape.width
