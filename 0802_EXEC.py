"""
EXEC allows arbitrary input to be compiled and run.  It essentially allows data to be run as code!
It is a function is used for the dynamic execution of Python program which can either be a string or object code.
If it is a string, the string is parsed as a suite of Python statements which is then executed unless a syntax error
occurs and if it is an object code, it is simply executed.
"""
# # Example 1 - manipulating program variables
# a = None
# exec('a = 1 + 2')
# print(a)    # Note how this actually changes the variable value - more destructive than the eval() function!


# # Example 2 - writing new functions
# exec("def test(): print('This function does not exist in our program scope... or does it?')")
# test()


# # Example 3 - Multi-line functions
# exec("""
# def quine():
#     print(open(__file__).read())
# """)
# quine()


# # Example 4 - importing other packages
# exec("""
# def bad_news():
#     import subprocess
#     subprocess.call(r"dir C:\Windows", shell=True)
# """)
# bad_news()
