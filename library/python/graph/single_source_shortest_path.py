#!/usr/bin/env pypy3

"""Computing single-source shortest paths of a graph without negative edges using Dijkstra's method.

Verification: [Shotest Path](https://judge.yosupo.jp/submission/12078)
"""


import heapq


# The value representing "infinity."
INF = 1000000000000000000


def dijkstra(num_vertices, adj_list, source=0):
    """Computing single-source shortest paths of the given graph without negative edges using Dijkstra's method.

    Parameters:

    - `num_vertices`: the number of nodes.
    - `adj_list`: the adjacency list.
    - `source`: the source node.

    Returns (as a tuple):

    - `dist`: a list such that `dist[i]` is the shortest distance from
      the vertex `source` to the vertex `i`.
    - `prev`: a list for reconstructing shortest paths.
    """

    dist = [INF for _ in range(num_vertices)]
    dist[source] = 0
    pq = [(dist[source], source)]
    heapq.heapify(pq)
    prev = [None for _ in range(num_vertices)]
    while pq:
        c, u = heapq.heappop(pq)
        if dist[u] < c:
            continue
        for v, cost in adj_list[u]:
            new_length = dist[u] + cost
            if new_length < dist[v]:
                dist[v] = new_length
                heapq.heappush(pq, (new_length, v))
                prev[v] = u
    return dist, prev
