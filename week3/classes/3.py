class Shape:
    def area(self):
        print(0)

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
    def area(self):
        print(self.length * self.width)
a=int(input())
b=int(input())
rctg = Rectangle(a, b)
rctg.area()