import math
class Point:
    def __init__(self,_x,_y,_x1,_y1):
        self.x = _x
        self.y = _y
        self.x1 = _x1
        self.y1 = _y1
       
    def show(self):
        print(f'first point coordinates : {self.x} - {self.y} and second point coordinates : {self.x1} - {self.y1}')
    def  dist(self):
        return math.sqrt(pow(self.x1-self.x,2) + pow(self.y1-self.y,2))
    def move(self):
        self.x1 = int(input())
        self.x = int(input())
        self.y1 = int(input())
        self.y = int(input())
p = Point(1,1,8,9)
print (p.dist())
p.show()
