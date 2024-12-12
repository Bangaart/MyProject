
class Point:

    def __init__(self, x,y):
        self.x = x
        self.y = y

    # def __eq__(self, other):
    #     return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

a1 = Point(1,2)
a2 = Point(1,2)
print(hash(a1), hash(a2))
print(a1 == a2)
d = {}
d[a1] = 4
d[a2] = 5
print(d)