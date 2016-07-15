#!/usr/bin/env python3

import array
import math
import random


def is_prime_trial_division(n):
    """Determing whether the given integer is prime by trial division.

    :param int n: The integer to be checked.
    :return: Whether n is prime or not.
    :rtype: bool
    """

    if n < 2:
        return False
    else:
        for i in range(2, n):
            if i * i > n:
                break
            elif n % i == 0:
                return False
        return True


def sieve_of_eratosthenes(end, typecode="L"):
    """Enumerates the prime numbers below the given integer.

    :param int end: Prime numbers below this integer will be enumerated.
    :param str typecode: The type of the array to be returned (optional).
    :return: The array of the prime numbers.
    :rtype: :class:`array.array`
    """

    assert end > 1
    is_prime = array.array("B", (True for i in range(end)))
    is_prime[0] = False
    is_prime[1] = False
    primes = array.array(typecode)
    for i in range(2, end):
        if is_prime[i]:
            primes.append(i)
            for j in range(2 * i, end, i):
                is_prime[j] = False
    return primes


def segment_sieve(begin, end, typecode="L"):
    """Enumerates the prime numbers in [begin, end).

    :param int begin: The beginning of the interval.
    :param int end: The end of the interval.
    :param str typecode: The type of the array to be returned (optional).
    :return: The array of the prime numbers.
    :rtype: :class:`array.array`
    """
    assert begin > 1
    assert begin <= end
    sqrt_end = math.ceil(math.sqrt(end))
    is_prime_small = array.array("B", (True for i in range(sqrt_end)))
    is_prime_small[0] = False
    is_prime_small[1] = False
    is_prime = array.array("B", (True for i in range(end - begin)))
    for i in range(2, sqrt_end):
        if is_prime_small[i]:
            for j in range(2 * i, sqrt_end, i):
                is_prime_small[j] = False
            for k in range(max(2, (begin + i - 1) // i) * i, end, i):
                is_prime[k - begin] = False
    primes = array.array(typecode,
                         (i for i, cond in enumerate(is_prime, begin) if cond))
    return primes


def is_prime_miller_rabin(n, k=50):
    """Determing whether the given integer is prime by the Miller-Rabin test.

    :param int n: The integer to be checked.
    :param int k: The parameter representing the accuracy of the determination.
    :return: Whether n is prime or not.
    :rtype: bool
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


def factorize_trial_division(n, typecode="L"):
    """Factorizes the given integer in prime numbers by trial division.

    :param int n: The integer to be factorized.
    :param str typecode: The type of the array to be returned (optional).
    :return: The array of factors.
    :rtype: :class:`array.array`
    """
    factors = array.array(typecode)
    if n < 2:
        return factors
    for p in sieve_of_eratosthenes(math.ceil(math.sqrt(n)) + 1):
        if p * p > n:
            break
        while n % p == 0:
            factors.append(p)
            n //= p
    if n > 1:
        factors.append(n)
    return factors
