"""Classes of objects for pack the box."""


class Container(object):

    def __init__(self, height=600, width=500):
        self.height = height
        self.width = width
        self.items = []
        self.matrix = []

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

    def initialize_matrix(self):
        """Sets matrix size equal to height and width."""

        for i in range(self.height):
            self.matrix.append([])
            for j in range(self.width):
                self.matrix[i].append(False)

        return self.matrix

    def cell_available(self,shape,x,y):
        """Checks matrix cell value: if False, new item is placed and cell value updated to True."""

        cells = []

        for h in range(shape.height):
            for w in range(shape.width):
                i = int((self.height/2) - y) + int(h - (self.height/2))
                j = int((self.width/2) + x) + int(w - (self.width/2))
                if not self.matrix[i][j]:
                    cells.append((i,j))
                    continue
                else:
                    return False

        for cell in cells:
            i = cell[0]
            j = cell[1]
            self.matrix[i][j] = True

        return True


class Shape(object):
    def __init__(self, *args):
        if len(args) == 1:
            self.type = 'circle'
            self.radius = args[0]
            self.height = 2 * args[0]
            self.width = 2 * args[0]
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
