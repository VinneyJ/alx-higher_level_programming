#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    count = len(argv) - 1
    print("{} argument{}".format(count, "s:" if count > 1 else ":" if count == 1 else "."))
    for i, arg in enumerate(argv[1:]):
        print("{}: {}".format(i + 1, arg))
