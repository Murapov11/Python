class Shape:
    def __init__(self, len):
        self.length = len
    def area(self):
        return self.length * self.length
class Rectangle(Shape):
    def __init__(self,_length,_width):
        self.length = _length
        self.width = _width
    def area(self):
        return self.length * self.width
s = Rectangle(5,6)
print(s.area())        


