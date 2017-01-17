"""Classes of objects for pack the box."""


class Container(object):

    def __init__(self, height=600, width=500):
        self.height = height
        self.width = width
        self.items = []

    def is_square(self):
        """Returns true if height and width are equal."""

        if self.height == self.width:
            return True
        return False

    def track_items(self):
        """Returns items currently in container."""

        return self.items

    def count_items(self):
        """Returns number of items successfully fit into container."""

        return len(self.items)

    def add_item(self, placed_item):
        """Adds item to container."""

        self.items.append(placed_item)
        return self.items


class Shape(object):
    def __init__(self, *args):
        if len(args) == 1:
            self.type = 'circle'
            self.radius = args[0]
        elif len(args) == 2:
            self.type = 'rectangle'
            self.height = args[0]
            self.width = args[1]

    def is_square(self):
        """Returns true if height and width are equal."""

        if self.height == self.width:
            return True
        return False

    def get_bb(self,x,y):
        """Returns bounding box of shape in terms of container coordinates (top,bottom,left,right)."""

        bb = (y,y-self.dimension,x,x+self.dimension)
        return bb
