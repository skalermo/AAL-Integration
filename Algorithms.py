"""Algorithms for graph coloring"""


import collections
from itertools import product
from random import choice


def bruteForce(graph, start=1):
    n = graph.getVertexCount()
    coloring = ()
    colorCount = 0
    for k in range(start-1, n):
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

    removeBadVertices(g)
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


def getLargestCliqueSize(g):
    """Return size of the largest clique in the graph g"""

    maxSize = [0]
    calcMaxCliqueSize([], list(g.adjDict.keys()), [], g, maxSize)
    return maxSize[0]


def calcMaxCliqueSize(R, P, X, g, maxCliqueSize):
    """Modified Bron-Kerbosch algorithm with pivoting
for finding size of the largest clique
    :param maxCliqueSize Wrapped in list variable
which will contain the result of the algorithm
    """

    if not any((P, X)):
        if len(R) > maxCliqueSize[0]:
            maxCliqueSize[0] = len(R)
    if not P:
        return

    # Choose random vertex from union of P and X as a pivot
    pivot = choice(P + X)

    for v in P[:]:
        if v not in g.adjDict[pivot]:
            R_v = R + [v]
            P_v = [v1 for v1 in P if v1 in g.adjDict[v]]
            X_v = [v1 for v1 in X if v1 in g.adjDict[v]]
            calcMaxCliqueSize(R_v, P_v, X_v, g, maxCliqueSize)
            P.remove(v)
            X.append(v)


def WelshPowell(graph):
    """Get coloring of the graph and number of used colors
    Implementation of the Welsh Powell algorithm"""

    removeBadVertices(graph)
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


def removeBadVertices(graph):
    """Remove all vertices with degree n-1"""

    for v in list(graph.adjDict):
        if len(graph.adjDict[v]) == graph.getVertexCount() - 1:
            graph.removeVertex(v)
