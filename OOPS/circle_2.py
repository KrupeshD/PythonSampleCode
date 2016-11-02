class Circle:
    def __init__(self,radius=1):
        self.radius = radius  #radius is an instance variable of class Circle
    def area(self):
        return self.radius * self.radius * 3.14159

#c = Circle(5)
c = Circle()
print(c.area())