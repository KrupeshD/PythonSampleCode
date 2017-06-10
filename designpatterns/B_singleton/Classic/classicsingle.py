class Singleton(object):

    """__new__ is the first step of instance creation. It's called first, and is responsible for returning a
    new instance of your class. In contrast, __init__ doesn't return anything; it's only responsible for initializing
    the instance after it's been created."""

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

# Classic singleton is not good enough in inheritance. Use Borg instead.
# If you expect that your singleton will not be inherited then use Classic. Otherwise stick to Borg.
