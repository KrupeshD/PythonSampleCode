from mathproj import version
from mathproj.comp import c1
#from mathproj.comp.numeric.n2 import h
from .n2 import h

def g():
    print("Version is",version)
    print("X is",c1.x)
    print(h())