#!/usr/bin/python3
import sys
import inspect

def print_names():
    module = sys.modules[__name__]
    members = inspect.getmembers(module)
    names = [name for name, _ in members if not name.startswith("__")]
    names.sort()
    
    for name in names:
        print(name)

if __name__ == "__main__":
    print_names()
