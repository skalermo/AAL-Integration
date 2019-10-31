"""Algorithms for graph coloring"""


def bruteForceKcolor(graph, k):
    """Check every possible k coloring of the graph
    :param graph The input graph
    :param k Number of colors to deal with"""

    # todo rewrite it using itertools.product

    colorTable = dict.fromkeys(graph.adjDict.keys(), 0)
    bc = 0
    tries = 0
    while True:
        if bc > 0:
            tries += 1
            test = True
            for v in graph.adjDict:
                for n in graph.adjDict[v]:
                    if colorTable[v] == colorTable[n]:
                        test = False
                        break
                if not test:
                    break
            if test:
                break

        while True:
            j = 0
            for i in colorTable.keys():
                colorTable[i] += 1
                if colorTable[i] == k - 1:
                    bc += 1
                if colorTable[i] < k:
                    break
                colorTable[i] = 0
                bc -= 1
                j += 1

            if j < graph.getVertexCount():
                break
            return {}
    return colorTable, k


def bruteForce(graph):
    n = graph.getVertexCount()
    solution = ()
    for k in range(2, n+1):
        solution = bruteForceKcolor(graph, k)
        if solution:
            break
    return solution
