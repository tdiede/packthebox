""" Pack the box.

container: The container can either be a square or a rectangle.
Parameters to define the container are: square = true or false, h_size, v_size

item: The item can be a square, a rectangle, or a circle.
Parameters to define the item are: shape = 0, 1, 2; h_size, v_size, or radius if circle
"""


import random

import turtle

from classes import Container, Shape


screen = turtle.getscreen()
screen.title("Pack the box!")
screen.bgcolor("#80A080")
screen.setup(width=0.5, height=0.8, startx=50, starty=None)

turtle.speed(0)


def create_container():

    height = input("What is the height of your container? default:600 >>")
    width = input("What is the width of your container? default:500 >>")
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


def pad_container():
    """Pads container bounds according to size of item."""

    if vars(shape)['type'] == 'circle':
        return shape.radius, 0, shape.radius, shape.radius*2
    elif vars(shape)['type'] == 'rectangle':
        return shape.height/2, shape.width/2, shape.height/2, shape.width/2


def no_overlap(x,y):
    """Checks whether new item fits in container at specified random coordinate.
    Checks to make sure new item does not overlap with any existing item."""

    if vars(shape)['type'] == 'circle':
        # for item in container.items:
        return True
    elif vars(shape)['type'] == 'rectangle':
        for item in container.items:
            center = item.get('coordinates')
            print (center)
            if x > (center['x'] - (shape.width)) and x < (center['x'] + (shape.width)) and y > (center['y'] - (shape.height)) and y < (center['x'] + (shape.height)):
                return False
            else:
                continue
        return True


def gen_random_item():
    """Generates a random type of next item to keep adding to container."""

    shape_key = gen_random_shape()

    if shape_key == 0:
        dimensions = input("What is the desired height/width of your rectangle? default:20,10 >>") or '20,10'
        height, width = dimensions.split(',')
        shape = Shape(int(height), int(width))
        # draw_rect(shape)

    elif shape_key == 1:
        radius = input("What is the desired radius of your circle? default:10 >>") or '10'
        shape = Shape(int(radius))
        # draw_circle(shape)

    return shape


def place_items():

    x,y = gen_random_coord()

    # if not within_container(x,y):
    #     label_coordinates(x,y)
    #     x,y = gen_random_coord()

    while no_overlap(x,y):

        if vars(shape)['type'] == 'circle':
            draw_circle(shape,x,y)
        elif vars(shape)['type'] == 'rectangle':
            draw_rect(shape,x,y)

        container.add_items(shape,x,y)
        print (container.items)

        x,y = gen_random_coord()

    x,y = gen_random_coord()


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

def gen_random_coord():

    padding = pad_container()

    top_limit = container.height/2 - padding[0]
    bottom_limit = container.height/2 + padding[2]
    left_limit = container.width/2 + padding[3]
    right_limit = container.width/2 - padding[1]

    scale_x = random.random()
    scale_y = random.random()

    direction_x = random.choice([-1,1])
    direction_y = random.choice([-1,1])

    if direction_x == -1:
        x = round(left_limit * scale_x * direction_x, 2)
    elif direction_x > 0:
        x = round(right_limit * scale_x * direction_x, 2)

    if direction_y <= 0:
        y = round(bottom_limit * scale_y * direction_y, 2)
    elif direction_y > 0:
        y = round(top_limit * scale_y * direction_y, 2)

    print (x,y)
    return x,y


def gen_random_shape():

    shape_key = random.randrange(0,2,1)
    return shape_key


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
