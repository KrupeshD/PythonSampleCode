class Color:
    def __init__(self,red,green,blue):
        self._red = red
        self._green = green
        self._blue = blue

    def __str__(self): #__str__ is the special method attribute. it returns human readable representation of the object.
        return "Color : R={0:d}, G={1:d}, B={2:d}".format(self._red,self._green,self._blue)

c = Color(34,45,67)
print(c)
