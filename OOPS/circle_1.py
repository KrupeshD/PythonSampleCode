class Circle:
    def __init__(self):
        self.radius = 1 #radius is an instance variable of class Circle
    def area(self):
        return self.radius * self.radius * 3.14159

c = Circle()
#c.radius=3
print(c.area())