import Graph


def parseInput(textToParse):
    g = Graph.Graph()
    for line in textToParse:
        words = line.split()
        if len(words) == 1:
            g.addVertex(words[0])
        elif len(words) == 2:
            g.addEdge(words[0], words[1])
        else:
            raise ValueError('Error: Incorrect input format')
    return g
