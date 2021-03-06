#!/usr/bin/env python3

"""Computes all pairs shortest paths in a graph using the Warshall-Floyd algorithm.

Verification: [GRL_1_C](https://onlinejudge.u-aizu.ac.jp/status/users/hamukichi/submissions/1/GRL_1_C/judge/4573276/Python3)
"""


import itertools


# the value which represents "infinity."
INF = 10 ** 10


def in_place_warshall_floyd(adj_matrix):
    """Solves the all-pairs shortest path problem using the Warshall-Floyd algorithm.

    The adjacency matrix A of the graph. This object must be
    able to be treated as a $n \times n$ matrix. $A_{i, j}$ represents the
    cost of the edge $i \rightarrow j$. If $A_{i, j}$ is `INF`` or more,
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


def dist_to_str(d):
    if d < INF:
        return str(d)
    else:
        return "INF"


def main():
    v, e = (int(z) for z in input().split())
    adj_matrix = [[INF for _ in range(v)] for _ in range(v)]
    for i in range(v):
        adj_matrix[i][i] = 0
    for _ in range(e):
        s, t, d = (int(z) for z in input().split())
        adj_matrix[s][t] = d
    has_nc = in_place_warshall_floyd(adj_matrix)
    if has_nc:
        print("NEGATIVE CYCLE")
    else:
        for line in adj_matrix:
            print(*(dist_to_str(d) for d in line))


if __name__ == '__main__':
    main()