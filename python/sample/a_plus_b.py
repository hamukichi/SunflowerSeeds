#!/usr/bin/env python3

"""Library for adding the given two integers.

This library is just a sample and you usually do not need to use it.
"""


def add_two_integers(a, b):
    """Adds the given two integers and returns the result.
    """

    return a + b


def main():
    """Answers [A + B](https://judge.yosupo.jp/problem/aplusb) using `add_two_integers`.
    """
    a, b = (int(z) for z in input().split())
    res = add_two_integers(a, b)
    print(res)


if __name__ == '__main__':
    main()