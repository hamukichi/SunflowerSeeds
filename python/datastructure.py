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


class UnionFind(object):

    def __init__(self, number_of_nodes):
        self.par = list(range(number_of_nodes))
        self.rank = [0] * number_of_nodes

    def root(self, node):
        if self.par[node] == node:
            return node
        else:
            r = self.root(self.par[node])
            self.par[node] = r
            return r

    def in_the_same_set(self, node1, node2):
        return self.root(node1) == self.root(node2)

    def unite(self, node1, node2):
        x = self.root(node1)
        y = self.root(node2)
        if x != y:
            if self.rank[x] < self.rank[y]:
                x, y = y, x
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
