#!/usr/bin/env python3
# https://judge.yosupo.jp/problem/unionfind


class UnionFind(object):
    """A simple implementation of disjoint-set data structures.
    """


    def __init__(self, number_of_nodes):
        """Create a disjoint-data structure with `number_of_nodes` nodes.
        """
        self.par = list(range(number_of_nodes))
        self.rank = [0] * number_of_nodes

    def root(self, node):
        """Returns the root of node #`node`.
        """
        if self.par[node] == node:
            return node
        else:
            r = self.root(self.par[node])
            self.par[node] = r
            return r

    def in_the_same_set(self, node1, node2):
        """See if the given two nodes #`node1` and #`node2` are in the same set.
        """
        return self.root(node1) == self.root(node2)

    def unite(self, node1, node2):
        """Unite the set containing node #`node1` and the another set containing node #`node2`.
        """
        x = self.root(node1)
        y = self.root(node2)
        if x != y:
            if self.rank[x] < self.rank[y]:
                x, y = y, x
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1


def process_queries(n, queries):
    uf = UnionFind(n)
    for t, u, v in queries:
        if t == 0:
            uf.unite(u, v)
        else:
            yield uf.in_the_same_set(u, v)


def main():
    n, q = (int(z) for z in input().split())
    queries = []
    for _ in range(q):
        queries.append(tuple(int(z) for z in input().split()))
    for res in process_queries(n, queries):
        print(int(res))


if __name__ == '__main__':
    main()