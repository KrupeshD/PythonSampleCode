def example_fun(x,y,**others):
    """
    :param x: parameter1
    :param y: parameter2
    :param others: all other named parameters are stored as dictionary object. Use of **
    :return: nothing
    """

    print("x:{0}, y:{1}, keys in 'others':{2}".format(x,y,list(others.keys())))
    others_total=0
    for k in others.keys():
        others_total = others_total + others[k]
    print("The toal of values in 'others' is:{0}".format(others_total))

example_fun(3,4,p1=67,p2=20,p3=1)

