#!/usr/bin/python3

def uniq_add(my_list=None):
    if my_list is None:
        my_list = []

    new_list = set(my_list)
    total = 0
    for item in new_list:
        total += item

    return total


my_list = [1, 2, 3, 1, 4, 2, 5]
result = uniq_add(my_list)
print("Result: {:d}".format(result))
