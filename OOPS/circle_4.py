"""
circle_4 module : contains Circle class with static methods.
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

    @staticmethod # @staticmethod is a decorator of python.
    def total_area():
        """
        :return: total area of all circles created
        """
        total = 0
        for c in Circle.all_circles:
            total = total + c.area()
        return total


print (Circle.total_area()) # calling static method before creating any instance of the class
c1 = Circle(3)
print(c1.area())
print(c1.total_area()) # calling static method using instance of the class
c2 = Circle(5)
print(c2.area())
print (Circle.total_area()) # calling static method using class name.