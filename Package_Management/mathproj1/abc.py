from mathproj1 import version
x = 1.0

def h():
    return "Called function h in module abc"

def g():
    print("Version is",version)
    print("X is",x)
    print(h())

class test1:
    a = 10
    def get_a(self):
        return self.a
