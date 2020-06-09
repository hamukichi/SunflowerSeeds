#!/usr/bin/env python3

"""Implements disjoint-set data structures (so-called union-find data structures).
"""


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


def main():
    pass


if __name__ == '__main__':
    main()