def forty():
    """
    generator functions creates your own iterators. Generates a value using yield in each call.
    This function generates number 0 to 40. one value per call.
    Values of local variables are saved from one call to the next, unlike the normal function.
    """
    x=0
    while x < 40:
        print("In Generator: x = ",x)
        yield x
        x+=1

for i in forty():
    print(i)

print(2 in forty())
print(50 in forty())