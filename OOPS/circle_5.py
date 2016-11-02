"""
circle_5 module : contains Circle class with static methods.
"""
class Circle:
    """Circle Class"""
    all_circles = [] # Variable containing the list of all Circle instances created
    pi=3.1415999 # pi is the class variable here. belong to the class and not the instance.
    def __init__(self,r=1):
        """Creates a circle with the given radius"""
        self.radius = r
        self.all_circles.append(self) #add the instace to the all_cirle list as it is created.
    def area(self):
        """
        :return: Area of the circle
        """
        return self.__class__.pi * self.radius * self.radius

    @classmethod # @staticmethod is a decorator of python.
    def total_area(cls):
        """
        :return: total area of all circles created
        """
        total = 0
        for c in cls.all_circles: #no need to use class name here unlike static method.
            total = total + c.area()
        return total


print (Circle.total_area()) # calling static method before creating any instance of the class
c1 = Circle(4)
print(c1.area())
print(c1.total_area()) # calling static method using instance of the class
c2 = Circle(9)
print(c2.area())
print (Circle.total_area()) # calling static method using class name.