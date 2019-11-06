class Graph:
    """Graph implementation based on dictionary of sets"""

    def __init__(self):
        self.adjDict = {}
        self.edgeCount = 0

    def __str__(self):
        output = ''
        for k, i in self.adjDict.items():
            output += '\n' + str(k) + ': ' + str(i)
        return output

    def addVertex(self, v):
        if v not in self.adjDict:
            self.adjDict[v] = set()

    def addVertices(self, vertices):
        for v in vertices:
            self.addVertex(v)

    def removeVertex(self, v):
        if v not in self.adjDict:
            return

        self.edgeCount -= len(self.adjDict[v])
        for neighbor in self.adjDict[v]:
            self.adjDict[neighbor].remove(v)
        del self.adjDict[v]

    def addEdge(self, u, v):
        """Add edge between u and v vertices
        Do nothing if vertices are the same
        or if at least one of them doesn't belong to the graph"""

        if u == v or \
                v not in self.adjDict or\
                u not in self.adjDict:
            return

        le = len(self.adjDict[v])
        self.adjDict[v].add(u)
        self.adjDict[u].add(v)

        edgeAdded = len(self.adjDict[v]) != le
        if edgeAdded:
            self.edgeCount += 1

    def addEdges(self, edges):
        for edge in edges:
            self.addEdge(edge[0], edge[1])

    def removeEdge(self, v, u):
        if u == v or \
                v not in self.adjDict or \
                u not in self.adjDict:
            return

        self.adjDict[v].remove(u)
        self.adjDict[u].remove(v)
        self.edgeCount -= 1

    def getVertexCount(self):
        return len(self.adjDict)

    def getEdgeCount(self):
        return self.edgeCount

    def connected(self, u, v):
        return u in self.adjDict[v]
