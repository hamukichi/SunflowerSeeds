#!/usr/bin/env python3

import enum


EPS = 1e-10


class PointsRelation(enum.Enum):
    counter_clockwise = 1
    clockwise = 2
    online_back = 3
    on_segment = 4
    online_front = 5


def inner_product(v1, v2):
    return v1.real * v2.real + v1.imag * v2.imag


def outer_product(v1, v2):
    return v1.real * v2.imag - v1.imag * v2.real


def project(a, b):
    return a * inner_product(a, b) / (abs(a) ** 2)


def points_relation(p0, p1, p2):
    v1 = p1 - p0
    v2 = p2 - p0
    op = outer_product(v1, v2)
    if op > EPS:
        return PointsRelation.counter_clockwise
    elif op < -EPS:
        return PointsRelation.clockwise
    elif inner_product(v1, v2) < -EPS:
        return PointsRelation.online_back
    elif abs(v1) < abs(v2):
        return PointsRelation.online_front
    else:
        return PointsRelation.on_segment

        
def in_place_convex_hull_andrew(ps):
    def judge(p0, p1, p2):
        b = points_relation(p0, p1, p2) != PointsRelation.counter_clockwise
        b &= points_relation(p0, p1, p2) != PointsRelation.online_front
        return b
    if len(ps) < 3:
        return ps
    ps.sort(key=lambda p: p.imag)
    n = len(ps)
    k = 0
    ch = [None for _ in range(2 * n)]
    for i in range(n):
        while k >= 2 and judge(ch[k - 2], ch[k - 1], ps[i]):
            k -= 1
        ch[k] = ps[i]
        k += 1
    t = k + 1
    for i in range(n - 1)[::-1]:
        while k >= t and judge(ch[k - 2], ch[k - 1], ps[i]):
            k -= 1
        ch[k] = ps[i]
        k += 1
    ch = ch[:k - 1]
    return ch
