#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div


def main():
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    op = argv[2]

    op_dict = {'+': add, '-': sub, '*': mul, '/': div}
    if op not in op_dict:
        print("Unkown operator. Available operators: +, -, * and /")
        exit(1)

    print("{:d} {:s} {:d} = {:d}".format(a, op, b, op_dict[op](a, b)))
    exit(0)

if __name__ == "__main__":
    main()
