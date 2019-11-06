"""Algorithms for graph coloring"""


import collections
from itertools import product
from random import choice


def bruteForce(graph):
    n = graph.getVertexCount()
    coloring = ()
    colorCount = 0
    for k in range(n):
        coloring = bruteForceKcolor(graph, k)
        if coloring:
            colorCount = k
            break
    return coloring, colorCount


def fastBruteForce(graph):
    n = graph.getVertexCount()
    coloring = ()
    colorCount = 0
    for k in range(getMaximumCliqueSize(graph)-1, n):
        coloring = bruteForceKcolor(graph, k)
        if coloring:
            colorCount = k
            break
    return coloring, colorCount


def bruteForceKcolor(g, k):
    """Check every possible k coloring of the graph g
    :param g The input graph
    :param k Number of colors to deal with
    """

    solution = {}
    indexedVertices = {v: k for k, v in dict(enumerate(g.adjDict)).items()}
    for coloring in product(range(k), repeat=g.getVertexCount()):
        found = True
        for v in g.adjDict:
            for u in g.adjDict[v]:
                if coloring[indexedVertices[v]] == coloring[indexedVertices[u]]:
                    found = False
                    break
            if not found:
                break
        if found:
            solution = {key: val for key, val in zip(g.adjDict.keys(), coloring)}
            break
    return solution


def getMaximumCliqueSize(g):
    """Return size of the largest clique in the graph g
    Function uses Bron Kerbosch algorithm"""

    maxSize = 0
    for clique in BronKerbosch2([], list(g.adjDict.keys()), [], g):
        if len(clique) > maxSize:
            maxSize = len(clique)
    return maxSize


def BronKerbosch2(R, P, X, g):
    """Bron Kerbosch algorithm with pivoting
    for finding all maximum cliques in given graph g"""

    if not any((P, X)):
        yield R
    if not P:
        return
    pivot = choice(P + X)
    for v in P[:]:
        if v not in g.adjDict[pivot]:
            R_v = R + [v]
            P_v = [v1 for v1 in P if v1 in g.adjDict[v]]
            X_v = [v1 for v1 in X if v1 in g.adjDict[v]]
            for r in BronKerbosch2(R_v, P_v, X_v, g):
                yield r
            P.remove(v)
            X.append(v)


def WelshPowell(graph):
    """Get coloring of the graph and number of used colors
    Implementation of the Welsh Powell algorithm"""

    notColored = list(collections.OrderedDict(sorted(graph.adjDict.items(),
                                                     key=lambda kv: len(kv[1]), reverse=True)).keys())
    lastColor = 0
    coloring = {}
    while len(notColored):
        skippedVertex = False
        coloring[lastColor] = [notColored[0]]
        for v in notColored[1:]:
            for coloredVertex in coloring[lastColor]:
                if graph.connected(v, coloredVertex):
                    skippedVertex = True
                    break
            if skippedVertex:
                continue
            coloring[lastColor].append(v)

        notColored = [x for x in notColored if x not in coloring[lastColor]]
        lastColor += 1

    return coloring, lastColor
