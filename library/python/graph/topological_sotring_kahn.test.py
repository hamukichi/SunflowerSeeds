#!/usr/bin/env python3

"""
Performs topological sorting of the given DAG using Kahn's algorithm.

Verification: [GRL_4_B](https://onlinejudge.u-aizu.ac.jp/status/users/hamukichi/submissions/1/GRL_4_B/judge/4573325/Python3)
"""

import heapq


class TopologicalSortError(Exception):
    """This exception is raised when something gets wrong while performing `topological_sort`.
    """    
    pass


def topological_sort_kahn(num_vs, adj_vs):
    """Performs topological sorting of the given DAG with modified Kahn's algorithm.

    This function computes the lexicographically least
    topological order of the given DAG.

    Parameters:

    - `num_vs`: The number of vertices of the DAG.
    - `adj_vs` The adjacency list of the DAG.

    Returns: the lexicographically least topological order as a list.
    
    Raises `TopologicalSortError` if the given graph is not a DAG.
    """
    
    in_deg = [0 for _ in range(num_vs)]
    for dests in adj_vs:
        for dest in dests:
            in_deg[dest] += 1
    sorted_vs = []
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
