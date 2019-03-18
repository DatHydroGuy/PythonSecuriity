import time
from random import randint


def check_password(guess_password):
    """
    Here, we emulate what happens 'under the hood' during a string comparison (or a comparison of any two iterables
    of data).  The basic premise is that a comparison is made between the first element of each iterable, and if they
    don't match, then a failure is returned.  If they do match, then the second elements are compared.  This continues
    until all elements match, or the length of one iterable is found to differ from the other.
    Crucially, the longer it takes to receive a failure, the "more correct" we know our guess is.  This is the heart
    of the timing attack.
    """
    actual_password = "potato"
    for i, char in enumerate(guess_password):
        if char != actual_password[i] or i > len(actual_password):
            return False
    return True


def time_candidate(candidate):
    """
    This function simply tests our guess against the actual password a number of times (500,000 in this case) and
    returns the average time for the "check_password" function to return.
    """
    # global candidates, _, t1, t2
    candidates = []
    for _ in range(size):
        check_password(str(randint(0, 99999999)))    # Clear any pre-fetch data in the CPU cache
        t1 = timer()
        check_password(candidate)
        t2 = timer()
        candidates.append(t2 - t1)
    print(f"Average time for '{candidate}' = {1000000000 * sum(candidates[upper:]) / len(candidates[upper:])} ns.")


timer = time.perf_counter  # requires Python 3.3 or later
alphabet = 'abcdefghijklmnopqrstuvwxyz'
size = 500000
upper = 0

time_candidate('a')

time_candidate('p')

time_candidate('pa')

time_candidate('po')

time_candidate('poa')

time_candidate('pot')

time_candidate('potx')

time_candidate('pota')

time_candidate('potaa')

time_candidate('potat')

time_candidate('potata')

time_candidate('potato')
