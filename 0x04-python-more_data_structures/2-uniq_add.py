def uniq_add(my_list=[]):
    new_list = set(my_list)
    total = 0
    for item in new_list:
        total += item
    return total

my_list = [1, 2, 3, 1, 4, 2, 5]
result = uniq_add(my_list)
print("Result: {:d}".format(result))
