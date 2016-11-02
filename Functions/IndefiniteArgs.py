def find_max(*numbers):
    """
    :param numbers: stores all(if any) sequential parameters as tuple object. Use of *
    :return:
    """
    if not numbers:
        return 0
    else:
        return max(numbers)

print(find_max())
print(find_max(1))
print(find_max(2,4,5,6))
print(find_max(6,4,3,44,55,66,7,3,22,111,8,5,4,88,55,66,999888,3432,2445))
my_list=[4,7,3,9,1]
print(find_max(my_list))
