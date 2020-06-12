#!/usr/bin/env python3

"""Determines whether an input integer is prime, using the Miller-Rabin test.

Verification: [ALDS1_1_C](https://onlinejudge.u-aizu.ac.jp/status/users/hamukichi/submissions/1/ALDS1_1_C/judge/4573080/Python3)
"""

import random


def is_prime_miller_rabin(n, k=50):
    """Determing whether the given integer `n` (> 0) is prime by the Miller-Rabin test.

    The parameter `k` represents the accuracy of the determination.
    """

    assert n > 0
    if n == 2:
        return True
    elif n == 1 or n % 2 == 0:
        return False
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for i in range(k):
        a = random.randint(1, n - 1)
        if pow(a, d, n) != 1:
            for r in range(0, s):
                if pow(a, d * 2 ** r, n) == n - 1:
                    break
            else:
                return False
    return True