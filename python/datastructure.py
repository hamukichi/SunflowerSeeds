#!/usr/bin/env python3

"""Implementation of data structures for competitive programming.
"""


import itertools


class CumulativeSum(object):
    """Constructs the cumulative sum of the elements in the given sequence.

    :param sequence: The sequence to be processed.
    :type sequence: sequence
    """

    def __init__(self, sequence):
        self.cumulative_sum = [0]
        self.cumulative_sum.extend(itertools.accumulate(sequence))

    def partial_sum(self, first, last):
        """Computes the partial sum of the sequence.

        :param first: The index representing the first element of the
                      subsequence.
        :type first: int
        :param last: The index representing the last element of the
                     subsequence.
        :return: The partial sum.
        """
        return self.cumulative_sum[last + 1] - self.cumulative_sum[first]
