#!/usr/bin/env python3

"""Determines whether an input integer is prime, by trial division.

Verification: [ALDS1_1_C](https://onlinejudge.u-aizu.ac.jp/status/users/hamukichi/submissions/1/ALDS1_1_C/judge/4573115/Python3)
"""


def is_prime_trial_division(n):
    """Determing whether the given integer `n` is prime by trial division.

    """

    assert n > 0
    if n < 2:
        return False
    else:
        for i in range(2, n):
            if i * i > n:
                break
            elif n % i == 0:
                return False
        return True
