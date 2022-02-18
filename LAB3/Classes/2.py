class Shape:
    def __init__(self, len):
        self.length = len
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, len):
        self.length = len
    def area(self):
        return self.length * self.length
#s = Square(5)
#print(s.area())