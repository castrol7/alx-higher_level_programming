#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            quotient = 0
            if i < len(my_list_1) and i < len(my_list_2):
                dividend = my_list_1[i]
                divisor = my_list_2[i]
                quotient = dividend / divisor
                if not isinstance(quotient, (int, float)):
                    raise TypeError
            elif i >= len(my_list_1) or i >= len(my_list_2):
                raise IndexError
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            result.append(quotient)
    return result
