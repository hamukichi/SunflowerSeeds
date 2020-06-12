#!/usr/bin/env python3

"""Computes all pairs shortest paths in a graph using the Warshall-Floyd algorithm.

Verification: [GRL_1_C](https://onlinejudge.u-aizu.ac.jp/status/users/hamukichi/submissions/1/GRL_1_C/judge/4573276/Python3)
"""


import itertools


# the value which represents "infinity."
INF = 1000000000000000000


def in_place_warshall_floyd(adj_matrix):
    r"""Solves the all-pairs shortest path problem using the Warshall-Floyd algorithm.

    The adjacency matrix A of the graph. This object must be
    able to be treated as a $n \times n$ matrix. $A_{i, j}$ represents the
    cost of the edge $i \rightarrow j$. If $A_{i, j}$ is `INF` or more,
    there is no edge between the two vertices. For all $x$, $A_{x, x} = 0$.
    Note that this matrix will be modified in place during calculation.
    
    Returns: whether the graph has a negative cycle.
    """

    n = len(adj_matrix)
    for k, i, j in itertools.product(range(n), repeat=3):
        if adj_matrix[i][k] == INF or adj_matrix[k][j] == INF:
            continue
        adj_matrix[i][j] = min(adj_matrix[i][j],
                               adj_matrix[i][k] + adj_matrix[k][j])
    return any(adj_matrix[i][i] < 0 for i in range(n))
