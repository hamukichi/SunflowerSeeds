#!/usr/bin/env python3

import itertools


#: The value which represents "infinity."
INF = 10 ** 8


def warshall_floyd(n, adj_matrix):
    """Solves the all-pairs shortest path problem using Warshall-Floyd method.

    :param int n: The number of vertices in the graph in question.
    :param adj_matrix: The adjacency matrix A of the graph. This object must be
                       able to be treated as a n * n matrix. Aij represents the
                       cost of the edge i -> j. If Aij is :const:`INF` or more,
                       there is no edge between i and j. For all x, Axx = 0.
                       Note that this matrix will be modified in place during
                       calculation.
    :return: The matrix which represents the result.
    """

    for k, i, j in itertools.product(range(n), repeat=3):
        adj_matrix[i][j] = min(adj_matrix[i][j],
                               adj_matrix[i][k] + adj_matrix[k][j])
    return adj_matrix
