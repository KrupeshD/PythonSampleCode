def decorator(func):
    print("In decorate function, decorating : ",func.__name__)
    def wrapper_func(*args):
        print("Executing : ",func.__name__)
        return func(*args)
    return wrapper_func

@decorator
def myfunction(parameter):
    print(parameter)

myfunction("Hello!")
#myfunction=decorator(myfunction) # When calling decorator without @
#myfunction("Hello!")