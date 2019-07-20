from math import hypot

class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector({x}, {y})'.format(x=self.x, y=self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(self.x or self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y* scalar)
# Using one magic method begets it's inverse
# does not combine though; having gt and eq will give you lt ne
# but not ge>=
    def __gt__(self, other):
        return hypot(self.x, self.y) >= hypot(other.x, other.y)

    def __eq__(self, other):
        return hypot(self.x, self.y) == hypot(other.x, other.y) 


