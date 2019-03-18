"""
EVAL is a function which allows a Python program to run code within itself.
It can be used to allow users to enter their own “scriptlets”: small expressions (or even small functions), that
can be used to customize the behavior of a complex system.
It is also sometimes used in applications needing to evaluate math expressions. This is much easier than writing
an expression parser.
"""
from math import *


def secret_function():          # Some other function within our program which holds sensitive information...
    return "Secret key is 42"


def function_creator():
    expression = input("Enter the function (in terms of x): y=")    # Expression to be evaluated, e.g. x*x+3

    x = int(input("Enter the value of x: "))                        # Variable used in expression, e.g. 4

    y = eval(expression)                                            # Evaluate expression

    print("y = {}".format(y))                                       # Print evaluated expression


if __name__ == "__main__":
    function_creator()
























# What happens if you enter secret_function() as the first input (and any number for the second)?


# What if our program had imported the subprocess module and we entered subprocess.call(r"dir C:\Windows", shell=True)
# for the first input (and any number for the second)?
