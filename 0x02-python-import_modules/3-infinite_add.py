#!/usr/bin/env python3
import sys

if __name__ == "__main__":
    args = sys.argv[1:]  # Get all command line arguments except the script name
    result = 0

    for arg in args:
        result += int(arg)

    print(result)
