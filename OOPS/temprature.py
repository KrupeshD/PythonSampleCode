class Temperature:
    def __init__(self):
        self.temp_ferh = 0

    @property # No need to use get n set methods like other OOPS languages.
    def temp(self):
        return (self.temp_ferh - 32) * 5 / 9

    @temp.setter
    def temp(self,new_temp):
        self.temp_ferh = new_temp * 9 / 5 + 32

t = Temperature()
print(t.temp_ferh)
print(t.temp)

t.temp = 43 # automatically converts to ferenhit from centigrade due to setter
print(t.temp_ferh)
print(t.temp)

t.temp_ferh = 100 # setting temperature in ferenhit and getting back in centigrade
print(t.temp)

