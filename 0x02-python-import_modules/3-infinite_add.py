#!/usr/bin/python3
from sys import argv

if __name__ == '__main__':
    add_num = 0
    for num in argv[1:]:
        add_num += int(num)
    print("{:d}".format(add_num))
