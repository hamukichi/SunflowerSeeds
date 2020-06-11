#!/usr/bin/env python3

"""Compute the prime factorization of the given integer by trial division.

Verification: [NTL_1_A](https://example.com)
"""

import math


def factorize_trial_division(n):
    """Compute the prime factorization of the given integer `n` by trival division.

    Returns: the prime factors as a list.
    """
    factors = []
    if n < 2:
        return factors
    for p in range(2, math.ceil(math.sqrt(n)) + 1):
        if p * p > n:
            break
        while n % p == 0:
            factors.append(p)
            n //= p
    if n > 1:
        factors.append(n)
    return factors