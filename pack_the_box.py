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


from random import random, randrange
from math import sqrt, pi

from classes import Container, Shape

import turtle


def create_container():
    """Asks user for dimensions and returns instance of Container class."""

    height = int(input("What is the height of your container? default:400 range:100-1000 >>> ") or 400)
    if height < 100 or height > 1000:
        height = 400
        print("Height needs to be in the range of 100 to 1000.  Default " + height + " selected.")
    width = int(input("What is the width of your container? default:400 range:100-1000 >>> ") or 400)
    if width < 100 or width > 1000:
        width = 400
        print("Width needs to be in the range of 100 to 1000.  Default " + width + " selected.")

    container = Container(height, width)
    return container


def create_shape():
    """Asks user for parameters to create instance of Shape class, which will be the item to keep adding to container."""

    # shape_key = gen_random_shape()
    shape_key = int(input("Enter shape type: 0 FOR RECT or 1 FOR CIRCLE. default:0 range:1-50 >>> ") or 0)

    if shape_key != 0 and shape_key != 1:
        shape_key = 0
        print("Selection needs to be 0 or 1.  Default " + shape_key + " selected.")

    if shape_key == 0:
        dimensions = input("Enter height,width of RECT or SQUARE to be inserted.  default:30,30 range:1-50 >>> ") or '30,30'
        height,width = [int(n) for n in dimensions.split(',')]
        if height < 1 or height > 50 or width < 1 or width > 50:
            height,width = 30,30
            print("Dimensions need to be in the range of 1 to 50.  Default " + height,width + " selected.")

        shape = Shape(height,width)

    elif shape_key == 1:
        radius = int(input("Enter radius of CIRCLE to be inserted.  default:15 range:1-25 ") or 15)
        if radius < 1 or radius > 25:
            radius = 15
            print("Radius needs to be in the range of 1 to 25.  Default " + radius + "selected.")

        shape = Shape(radius)

    return shape


def pack_item(limits):

    x,y = gen_random_coord(limits)

    if does_not_overlap(x,y):
        container.add_items(shape,x,y)
        return True

    return False


# def keep_packing():

#     attempts = 0

#     while True:
#         pack_item()
#         attempts += 1
#         if attempts >= 1000 + len(container.items):
#             print (attempts)
#             break


### TURTLE HELPER FUNCTIONS ###

def set_turtle():
    """Defines turtle interface."""

    screen = turtle.getscreen()
    screen.title("Pack the box!")
    screen.bgcolor("#80A080")
    screen.setup(width=0.5, height=0.8, startx=50, starty=None)

    turtle.speed(0)


def draw_container(container):
    """Turtle draws container instance."""

    turtle.shape('classic')
    turtle.color('', '')
    turtle.begin_fill()
    turtle.setheading(0)
    turtle.setpos(-int(container.width/2), int(container.height/2))
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
    turtle.setpos(x-int(shape.width/2), y+int(shape.height/2))
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


def draw_sequence():

    set_turtle()
    draw_container(container)

    for item in container.items:
        shape = item['item']
        coordinates = item['coordinates']['x'],item['coordinates']['y']
        label_coordinates(coordinates[0],coordinates[1])
        if vars(shape)['type'] == 'circle':
            draw_circle(shape,coordinates[0],coordinates[1])
        elif vars(shape)['type'] == 'rectangle':
            draw_rect(shape,coordinates[0],coordinates[1])


### HELPER FUNCTIONS ###

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


def pad_container(shape):
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


def does_not_overlap(x,y):
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

def calculate_container_area():
    return container.height * container.width


def calculate_shape_area():
    if vars(shape)['type'] == 'circle':
        return (shape.radius**2) * pi
    elif vars(shape)['type'] == 'rectangle':
        return shape.height * shape.width


def calculate_efficiency():
    container_area = calculate_container_area()
    shape_area = calculate_shape_area()
    return shape_area * len(container.items) / container_area


#############################################

if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    if not result.failed:
        print("ALL TESTS PASSED. GOOD WORK!")

    container = create_container()
    shape = create_shape()
    print(vars(container), container.is_square())
    print(vars(shape))

    limits = pad_container(shape)

    efficiency = calculate_efficiency()




    container = create_container()
    shape = create_shape()
    print ("Container height",container.height,"Container width",container.width)
    print ("Shape values", vars(shape))
    items_drawn = 0
    loop_limit = 100000
    total_not_drawn = 0
    consec_not_drawn = 0

    limits = pad_container()
    print("Now DRAWING !!")
    while True:
        if (place_item(limits)):  # Changed so that "program end" based on max num of consecutive overlaps
            items_drawn = items_drawn + 1
            consec_not_drawn = 0
        else:
            total_not_drawn = total_not_drawn + 1
            consec_not_drawn = consec_not_drawn + 1
            if (consec_not_drawn >= loop_limit):
                break
    print("number items drawn", items_drawn)
    print("consecutive items not drawn", consec_not_drawn)
    print("total items not drawn", total_not_drawn)
    container_area = container.height * container.width
    if vars(shape)['type'] == 'circle':
        eff = (items_drawn * (shape.radius**2) * pi) / container_area
    else:
        eff = (items_drawn * shape.height * shape.width) / container_area
    print("packing efficiency = ", eff*100,"%")



