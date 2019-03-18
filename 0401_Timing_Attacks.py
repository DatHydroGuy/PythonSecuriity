"""
Timing attacks are essentially a way of exposing the behaviour and algorithm by timing how long it takes to compare
provided values.
They are notoriously difficult to reproduce under "classroom" conditions because they are affected by all CPU
operations which may be running in the background.  They are usually run using a dedicated PC with a near-zero workload
from any other process.
"""


def check_password(password):
    return password == "potato"


guess = input("Enter password: ")

if check_password(guess):
    print("Correct!")
else:
    print("Wrong!")
