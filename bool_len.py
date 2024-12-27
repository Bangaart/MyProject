class Point:
    def __init__(self, x,y):
        self.x = x
        self.y = y

    def __len__(self):
        return 0
    def __bool__(self):
        print("bool")
        return self.x == self.y


b = Point(1,1)
print(bool(b))