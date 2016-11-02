class Shape:
    pi = 3.1451999
    def __init__(self,x,y):
        self.__x = x
        self.__y = y

        ## __x and __y are private variables. Any variable or method name that starts with __ but does not end with __ is private.

    def move(self,delta_x,delta_y):
        self.__x = self.__x + delta_x
        self.__y = self.__y + delta_y

class Circle(Shape): #Inherited Shape class
    def __init__(self,r=1,x=0,y=0):
        super().__init__(x,y)
        self.radius = r
    def area(self):
        return super().pi * self.radius * self.radius

class Square(Shape):
    def __init__(self,side=1,x=0,y=0):
        super().__init__(x,y)
        self.side = side
    def area(self):
        return self.side * self.side

"""c = Circle(3,6,7)
s = Square(5,10,12)

print("===================")
print("Circle Information")
print("===================")
#print("Circle located on the drawing surface at conrdinates ({0},{1})".format(c.x,c.y)) ## This will throw error as x and y are provate.
print("Area of the circle is: {0}".format(c.area()))
print("\n")

print("===================")
print("Square Information")
print("===================")
#print("Square located on the drawing surface at conrdinates ({0},{1})".format(s.x,s.y))
print("Area of the square is: {0}".format(s.area()))"""

