#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Get the first element of tuple_a and tuple_b
    a1 = tuple_a[0] if len(tuple_a) >= 1 else 0
    b1 = tuple_b[0] if len(tuple_b) >= 1 else 0

    # Get the second element of tuple_a and tuple_b
    a2 = tuple_a[1] if len(tuple_a) >= 2 else 0
    b2 = tuple_b[1] if len(tuple_b) >= 2 else 0

    # Compute the addition of the elements
    sum1 = a1 + b1
    sum2 = a2 + b2

    # Return the resulting tuple
    return (sum1, sum2)
