class vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return vector(self.x * other.x, self.y * other.y)

    def __truediv__(self, other):
        return vector(self.x / other.x, self.y / other.y)

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def norm(self):
        return (self.x**2 + self.y**2)**0.5
