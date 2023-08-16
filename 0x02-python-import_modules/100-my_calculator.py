#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys

if len(sys.argv) != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    sys.exit(1)

ops = {"+": add, "-": sub, "*": mul, "/": div}

if sys.argv[2] not in ops:
    print("Unknown operator. Available operators: +, -, * and /")
    sys.exit(1)

a = int(sys.argv[1])
b = int(sys.argv[3])
operator = sys.argv[2]
if operator == '/' and b == 0:
    print("Error: Division by zero is not allowed")
    sys.exit(1)

result = ops[operator](a, b)
print("{} {} {} = {}".format(a, operator, b, result))
