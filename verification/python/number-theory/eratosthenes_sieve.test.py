#!/usr/bin/env python3
# https://onlinejudge.u-aizu.ac.jp/status/users/hamukichi/submissions/1/0009/judge/4571021/Python3

"""Enumerates primes using the sieve of Eratosthenes.
"""


import sys


def sieve_of_eratosthenes(end):
    """Enumerates prime numbers below the given integer `end`.

    Returns (as a tuple):

        - `is_prime`: a list of bool values.
          If an integer `i` is a prime number, then `is_prime[i]` is True.
          Otherwise `is_prime[i]` is False.
        - `primes`: a list of prime numbers below `end`.
    """

    if end <= 1:
        raise ValueError("The integer `end` must be greater than one")
    is_prime = [True for _ in range(end)]
    is_prime[0] = False
    is_prime[1] = False
    primes = []
    for i in range(2, end):
        if is_prime[i]:
            primes.append(i)
            for j in range(2 * i, end, i):
                is_prime[j] = False
    return is_prime, primes



def main():
    ns = [int(n) for n in sys.stdin.readlines()]
    max_n = max(ns)
    is_prime, _ = sieve_of_eratosthenes(max_n + 1)
    for n in ns:
        print(sum(is_prime[:n + 1]))


if __name__ == '__main__':
    main()