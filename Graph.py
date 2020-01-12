class Graph:
    """Graph implementation based on dictionary of sets"""

    def __init__(self):
        """
        Graph constructor
        """
        self.adjDict = {}
        self.edgeCount = 0

    def __eq__(self, other):
        """
        Compare this graph to the other
        :param other: Compared graph
        :return: True if graphs are equal
        """
        if not isinstance(other, Graph):
            # don't attempt to compare against unrelated types
            return NotImplemented
        return self.adjDict == other.getAdjDict() and self.edgeCount == other.getEdgeCount()

    def addVertex(self, v):
        """
        Add vertex v to graph, if not already added
        :param v: Vertex to add

        """
        if v not in self.adjDict:
            self.adjDict[v] = []

    def addVertices(self, vertices):
        """
        Iteratively add vertices from the input list
        :param vertices: Input list of vertices

        """
        for v in vertices:
            self.addVertex(v)

    def removeVertex(self, v):
        """
        Remove vertex from graph. Decrease number of edges
        :param v: Vertex to remove

        """
        if v not in self.adjDict:
            return

        self.edgeCount -= len(self.adjDict[v])
        for neighbor in self.adjDict[v]:
            self.adjDict[neighbor].remove(v)
        del self.adjDict[v]

    def addEdge(self, u, v):
        """
        Add edge between u and v vertices
        Do nothing if vertices are the same
        or if at least one of them doesn't belong to the graph
        """

        if u == v or \
                v not in self.adjDict or\
                u not in self.adjDict:
            return

        edgeAdded = False
        if u not in self.adjDict[v]:
            self.adjDict[v].append(u)
            edgeAdded = True
        if v not in self.adjDict[u]:
            self.adjDict[u].append(v)
            edgeAdded = True

        if edgeAdded:
            self.edgeCount += 1

    def addEdges(self, edges):
        """
        Iteratively add edges from the input list
        :param edges: Input list of edges

        """
        for edge in edges:
            self.addEdge(edge[0], edge[1])

    def removeEdge(self, v, u):
        """
        Remove edge between u and v vertices
        Do nothing if vertices are the same
        or if at least one of them doesn't belong to the graph

        """
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
        """
        Check if the edge between vertices u and v exists

        """
        return u in self.adjDict[v]

    def getAdjDict(self):
        """
        Get dictionary containing vertices

        """
        return self.adjDict

    def getDict(self):
        """
        Get object's values
        """
        return self.__dict__

    def setDict(self, dict):
        """
        Set object's values
        :param dict: Assign object's values to the new ones from dict
        """
        self.__dict__ = dict

