"""
EXEC allows arbitrary input to be compiled and run.  It essentially allows data to be run as code!
It is a function is used for the dynamic execution of Python program which can either be a string or object code.
If it is a string, the string is parsed as a suite of Python statements which is then executed unless a syntax error
occurs and if it is an object code, it is simply executed.
"""

from math import *
misc_program = 'print("The factorial of 5 is:", factorial(5))'
exec(misc_program)
