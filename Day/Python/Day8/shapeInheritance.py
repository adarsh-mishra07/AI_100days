class Shape:
    def area(self):
        pass    #empty method 

class Rectangle(Shape):
    def area(self,w,h):
        return w*h
    
class Circles(Shape):
    def area(self,r):
        return 3.14*r*r
    
rect=Rectangle()
print(rect.area(4,5))

Circle=Circles()
print(Circle.area(3))