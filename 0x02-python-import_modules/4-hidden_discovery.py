#!/usr/bin/python3
import sys

if __name__ == "__main__":
    names = [name for name in dir() if not name.startswith("__")]
    names.sort()
    
    for name in names:
        print(name)
