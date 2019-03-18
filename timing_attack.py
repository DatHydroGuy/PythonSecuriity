import time


timer = time.perf_counter  # requires Python 3.3 or later
TEST_LOOPS = 1


def strcmp2(p1, p2):
    for i, c1 in enumerate(p1):
        if c1 < p2[i]:
            return -1

        if c1 > p2[i]:
            return 1

    return 0


def compare_strings(str1, str2):
    return strcmp2(str1, str2) == 0


def do_stat(pw_ref, test_pw, test_str):
    time_long = 0

    for i in range(TEST_LOOPS):
        start = timer()
        compare_strings(test_pw, pw_ref)
        end = timer()
        time_long += (end - start)

    if test_str:
        print(test_str, time_long / (i + 1))

    return time_long / (i + 1)


def time_attack_pw(correct_pw):
    calculated_string = " " * len(correct_pw)

    for i in range(len(correct_pw)):
        max_time_found = 0
        for j in 'abcdefghijklmnopqrstuvwxyz':
            current_char = j
            current_time = do_stat(correct_pw[i], current_char, None)

            if current_time > max_time_found:
                max_time_found = current_time
                calculated_string = calculated_string[:i] + j + calculated_string[(i + 1):]

    print("Guessed that pw should be: {0}\n".format(calculated_string))
    result = correct_pw == calculated_string

    return result


def main():
    correct_guesses = 0
    long_string = "thisisalongstring "
    short_string = "foo"

    print("Shows a couple of examples of the time it takes to make string comparison\n")
    do_stat(long_string, long_string, "avg time long string (thisisalongstring)")
    do_stat(short_string, short_string, "avg time short string (foo)")
    do_stat(short_string, "XXX", "avg time 0 char correct (XXX/foo)")
    do_stat(short_string, "fXX", "avg time 1 char correct (fXX/foo)")
    do_stat(short_string, "foX", "avg time 2 char correct (foX/foo)")
    do_stat(short_string, "foo", "avg time 3 char correct (foo/foo)")

    for i in range(len(long_string)):
        if time_attack_pw(long_string):
            correct_guesses += 1

    print("{0} successful timing attacks\n".format(correct_guesses))

    return 0


main()
