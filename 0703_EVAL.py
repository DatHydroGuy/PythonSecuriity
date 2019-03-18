"""
EVAL is a function which allows a Python program to run code within itself.
It can be used to allow users to enter their own “scriptlets”: small expressions (or even small functions), that
can be used to customize the behavior of a complex system.
It is also sometimes used in applications needing to evaluate math expressions. This is much easier than writing
an expression parser.

In general, DO NOT USE EVAL(), especially in conjunction with input() functions!
"""
from math import *


def secret_function():          # Some other function within our program which holds sensitive information...
    return "Secret key is 42"


def function_creator():
    expression = input("Enter the function (in terms of x): y=")    # Expression to be evaluated, e.g. x*x+3

    x = int(input("Enter the value of x: "))                        # Variable used in expression, e.g. 4

    safe_dict['x'] = x                                              # Adding variable x into our safe dictionary

    y = eval(expression, {"__builtins__": None}, safe_dict)         # Evaluate expression excluding global builtin
                                                                    # methods, and only permitting local methods
                                                                    # defined in our safe dictionary

    print("y = {}".format(y))                                       # Print evaluated expression


if __name__ == "__main__":
    # List of safe methods
    safe_list = ['acos', 'asin', 'atan', 'atan2', 'ceil', 'cos',
                 'cosh', 'degrees', 'e', 'exp', 'fabs', 'floor',
                 'fmod', 'frexp', 'hypot', 'ldexp', 'log', 'log10',
                 'modf', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt',
                 'tan', 'tanh']

    # Creating a dictionary of safe methods
    safe_dict = dict([(k, locals().get(k, None)) for k in safe_list])

    function_creator()
