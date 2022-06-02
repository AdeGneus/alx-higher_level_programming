#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv

    num_arg = len(argv) - 1

    if num_arg != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    op = argv[2]

    if op == "+":
        print("{} {} {} = {}".format(a, op, b, add(a, b)))
        exit(0)
    elif op == "-":
        print("{} {} {} = {}".format(a, op, b, sub(a, b)))
        exit(0)
    elif op == "*":
        print("{} {} {} = {}".format(a, op, b, mul(a, b)))
        exit(0)
    elif op == "/":
        print("{} {} {} = {}".format(a, op, b, div(a, b)))
        exit(0)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
