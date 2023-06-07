#!/usr/bin/python3
def uppercase(s):
    for c in s:
        if ord('a') <= ord(c) <= ord('z'):
            diff = ord('A') - ord('a')
            c = chr(ord(c) + diff)
        print("{}".format(c), end='')
    print()
