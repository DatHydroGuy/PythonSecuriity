"""
EXEC allows arbitrary input to be compiled and run.  It essentially allows data to be run as code!
It is a function is used for the dynamic execution of Python program which can either be a string or object code.
If it is a string, the string is parsed as a suite of Python statements which is then executed unless a syntax error
occurs and if it is an object code, it is simply executed.

In general, DO NOT USE EXEC(), especially in conjunction with input() functions!
"""
from math import *
misc_program = 'print("The factorial of 5 is:", factorial(5))'
exec(misc_program, {})      # Blank globals means that no functions can be executed (not very useful!)

# exec(misc_program, {"factorial":factorial})      # Whitelisted globals

# exec(misc_program, {}, {"factorial": factorial})      # Whitelisted locals


# To see what functions are available to an exec(), we can use the dir() function:
# exec("print(dir())", {"builtins": __builtins__}, {"sum": sum, "iter": iter})


# Example 1 - manipulating program variables
# a = None
# exec('a = 1 + 2', {})
# print(a)    # Note how this actually changes the variable value - more destructive than the eval() function!

# Note how we can use this to disable functions:
# exec('print(sum([1, 2]))', {"sum": None})

# or even to map function calls to invoke other functions!
# exec('print(sum([1, 2]))', {"sum": print})


# Example 2 - writing new functions
# exec("def test(): print('This function does not exist in our program scope... or does it?')", {"print": print})
# test()


# Example 3 - Multi-line functions
# exec("""
# def quine():
#     print(open(__file__).read())
# """, {"print": print})
# quine()


# Example 4 - importing other packages
# exec("""
# def bad_news():
#     import subprocess
#     subprocess.call(r"dir C:\Windows", shell=True)
# """, {"subprocess": None})
# bad_news()
