#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div
argv_len = len(sys.argv) - 1
if argv_len != 3:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)
elif sys.argv[2] == "*" or (len(sys.argv[2]) == 1 and ord(sys.argv[2]) == 42):
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if sys.argv[2] == "+":
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif sys.argv[2] == "-":
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif sys.argv[2] == "*":
        print("{} * {} = {}".format(a, b, mul(a, b)))
    elif sys.argv[2] == "/":
        print("{} / {} = {}".format(a, b, div(a, b)))
else:
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)
