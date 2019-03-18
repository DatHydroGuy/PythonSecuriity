import time
from secrets import compare_digest
from random import randint


# Fix: Use compare_digest from the secrets module
def check_password(password):
    return compare_digest(password, "potato")


def time_candidate(candidate):
    global candidates, _, t1, t2
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
