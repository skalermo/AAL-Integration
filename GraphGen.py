from random import seed, sample
from sys import argv


from Graph import Graph


def genEdges(n, d):
    """ Generate edges for graph
    :param n Vertex count in the graph
    :param d Density - ratio of number of edges in the graph
        to the number of edges in a N complete graph
    :return List of edges represented as tuples
    """

    edgeCountComplete = int(n*(n-1)/2)
    edgeCountToGenerate = int(edgeCountComplete * d)

    seed(100)
    return sample([(i, j,) for i in range(n-1) for j in range(i+1, n)], edgeCountToGenerate)


if __name__ == '__main__':
    """ Print generated graph to stdout
    Output example:
    1
    2
    3
    2 3
    1 3
    :arg argv[1] Number of vertices
    :arg argv[2] Density of graph"""

    if len(argv) != 3:
        print('Incorrect input')
        exit(1)
    vertexCount = int(argv[1])
    density = float(argv[2])
    edges = genEdges(vertexCount, density)
    for v in range(vertexCount):
        print(v)
    for edge in edges:
        print(edge[0], edge[1])
