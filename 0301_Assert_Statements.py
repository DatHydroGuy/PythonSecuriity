"""
Don’t use assert statements to guard against pieces of code that a user shouldn’t access.
By default, Python executes with __debug__ as true, but in a production environment it’s common to run with
optimizations. This will skip the assert statement!
"""


def check_access(user):
    assert user == 'admin', "User does not have access"
    print("Hello, admin")


user = "someone"

try:
    check_access(user)
except AssertionError as e:
    print(e.args[0])
