class Circle:
    pi=3.1415999 # pi is the class variable here. belong to the class and not the instance.
    def __init__(self,radius=1):
        self.radius = radius  #radius is an instance variable of class Circle
    def area(self):
        return self.radius * self.radius * self.__class__.pi # use self.__class__.<Class variable>

c = Circle(50)
#c = Circle()
print(c.area())