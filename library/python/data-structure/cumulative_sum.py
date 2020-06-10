#!/usr/bin/env python3

"""Cumulative sum.

Verification: [Static Range Sum](https://judge.yosupo.jp/submission/11777)
"""


import itertools


class CumulativeSum(object):
    """Constructs the cumulative sum of the elements in the given sequence.
    
    Parameters:

    - `sequence`: The sequence to be processed.
    """

    def __init__(self, sequence):
        self.cumulative_sum = [0]
        self.cumulative_sum.extend(itertools.accumulate(sequence))

    def partial_sum(self, first, last):
        """Computes the partial sum of the sequence.
        
        Parameters:

        - `first`: The index representing the first element of the subsequence.
        - `last`: The index representing the last element of the subsequence.
        
        Returns: the partial sum.
        """
        return self.cumulative_sum[last + 1] - self.cumulative_sum[first]
