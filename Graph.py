class Graph:
    """Graph implementation based on dictionary of sets"""

    def __init__(self):
        self.adjDict = {}
        # self.edgeCount = 0

    def __str__(self):
        output = ''
        for k, i in self.adjDict.items():
            output += '\n' + str(k) + ': ' + str(i)
        return output

    def addVertex(self, v):
        if v not in self.adjDict:
            self.adjDict[v] = set()

    def removeVertex(self, v):
        if v not in self.adjDict:
            return
        for neighbor in self.adjDict[v]:
            self.adjDict[neighbor].remove(v)
        del self.adjDict[v]

    def addEdge(self, *args):
        """Add edge represented as a tuple or 2 variables
        :param args There may be 1 (tuple) or 2 arguments"""

        if len(args) == 1 and isinstance(args[0], tuple):
            edge = args[0]
            self.addEdge(edge[0], edge[1])
            return
        elif len(args) != 2:
            return

        u = args[0]
        v = args[1]

        if u == v:
            return

        if v not in self.adjDict:
            self.adjDict[v] = {u}
        else:
            self.adjDict[v].add(u)
        if u not in self.adjDict:
            self.adjDict[u] = {v}
        else:
            self.adjDict[u].add(v)

        # self.edgeCount += 1

    def addEdges(self, edges):
        for edge in edges:
            self.addEdge(edge)
        # for edge in edges:
        #     if len(edge) == 2:
        #         self.addEdge(edge[0], edge[1])

    def removeEdge(self, v, u):
        if u == v or \
                v not in self.adjDict or \
                u not in self.adjDict:
            return

        self.adjDict[v].remove(u)
        self.adjDict[u].remove(v)
        # self.edgeCount -= 1

    def getVertexCount(self):
        return len(self.adjDict)

    def getEdgeCount(self):
        # return self.edgeCount
        """Iterate through the adjacency dictionary
        and sum the lengths of sets of vertices' neighbours divided by 2
        """
        return int(sum([len(i) for _, i in self.adjDict.items()]) / 2)
