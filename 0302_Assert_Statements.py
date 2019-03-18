"""
Fix: Only use assert statements to communicate with other developers, such as
in unit tests or to guard against incorrect API usage.
"""


def check_access(user):
    if user == 'admin':
        print("Hello, admin")
    else:
        raise AssertionError("User does not have access")


user = "someone"

try:
    check_access(user)
except AssertionError as e:
    print(e.args[0])
