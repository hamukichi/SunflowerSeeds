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


def main():
    n, m, s, t = (int(z) for z in input().split())
    adj_list = [set() for _ in range(n)]
    for _ in range(m):
        a, b, c = (int(z) for z in input().split())
        adj_list[a].add((b, c))
    dist, prev = dijkstra(n, adj_list, s)
    if dist[t] >= INF:
        print(-1)
    else:
        x = dist[t]
        cur = t
        path = [t]
        while cur != s:
            path.append(prev[cur])
            cur = prev[cur]
        path.reverse()
        y = len(path) - 1
        print(x, y)
        for i in range(y):
            print(path[i], path[i + 1])


if __name__ == '__main__':
    main()