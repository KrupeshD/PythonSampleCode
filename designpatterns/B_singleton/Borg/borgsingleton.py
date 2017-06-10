class Borg(object):
    _shared_state = {}

    """
    Python stores instance state in the __dict__ dictionary and when instantiated normally, every instance will
    have its own __dict__

    But in Borg Singleton, we deliberately assign the class variable _shared_state to all of the created instance.
    """

    def __new__(cls, *args, **kwargs):
        obj = super(Borg,cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_state
        return obj

# Basically __dict__ contains all the attributes which describe the object under question. It can be used to alter or read the attributes.


# Now, all successor of the Borg class (instances of child class) will always have share the same state.

class Child(Borg):
    pass

# See the output file. all child object share the parent's state.

# Descendant of the Borg class but has a different state, you can reset shared_state as follows:

class AnotherChild(Borg):
    _shared_state = {}
