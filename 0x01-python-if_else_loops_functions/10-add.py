#!/usr/bin/python3
def add(a, b):
    # Iterate until there is no carry
    while b != 0:
        # Calculate the carry
        carry = a & b

        # Sum of bits without considering carry
        a = a ^ b

        # Left shift the carry by 1 bit to add to the next position
        b = carry << 1

    return a
