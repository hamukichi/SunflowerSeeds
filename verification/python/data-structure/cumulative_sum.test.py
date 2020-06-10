#!/usr/bin/env python3


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


def process_queries(n, bs, queries):
    cs = CumulativeSum(bs)
    return (cs.partial_sum(l, r - 1) for l, r in queries)


def main():
    n, q = (int(z) for z in input().split())
    bs = [int(b) for b in input().split()]
    queries = [tuple(int(z) for z in input().split()) for _ in range(q)]
    print(*process_queries(n, bs, queries), sep="\n")


if __name__ == '__main__':
    main()