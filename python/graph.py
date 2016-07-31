#!/usr/bin/env python3

"""Contains implementation of graph algorithms.

"""

import array
import heapq
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


class TopologicalSortError(Exception):
    pass


def topological_sort(num_vs, adj_vs):
    """ Performs topological sorting of the given DAG.

    This function computes the lexicographically least
    topological order of the given DAG.

    :param num_vs int: The number of vertices.
    :param adj_vs list: The adjacency list.
    :return: The lexicographically least topological order.
    :rtype: :obj:`array.array`
    :raises TopologicalSortError: if the given graph is not a DAG
    """
    in_deg = array.array("L", (0 for _ in range(num_vs)))
    for dests in adj_vs:
        for dest in dests:
            in_deg[dest] += 1
    sorted_vs = array.array("L")
    pq = []
    for s in range(num_vs):
        if in_deg[s] == 0:
            heapq.heappush(pq, s)
    while pq:
        u = heapq.heappop(pq)
        sorted_vs.append(u)
        for v in adj_vs[u]:
            in_deg[v] -= 1
            if in_deg[v] == 0:
                heapq.heappush(pq, v)
    if all(x == 0 for x in in_deg):
        return sorted_vs
    else:
        raise TopologicalSortError("The graph has a cycle")
