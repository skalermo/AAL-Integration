from unittest import TestCase
import Graph


class TestGraph(TestCase):
    def testGraphInitSize(self):
        g = Graph.Graph()
        self.assertEqual(g.getVertexCount(), 0)
        self.assertEqual(g.getEdgeCount(), 0)
        self.assertDictEqual(g.adjDict, {})

    def test_addVertex(self):
        g = Graph.Graph()
        g.addVertex(1)
        self.assertEqual(g.getVertexCount(), 1)
        self.assertEqual(g.getEdgeCount(), 0)
        g.addVertex(1)
        self.assertEqual(g.getVertexCount(), 1)
        g.addVertex(2)
        g.addVertex(4)
        self.assertEqual(g.getVertexCount(), 3)
        self.assertDictEqual(g.adjDict, {
            1: [],
            2: [],
            4: []
        })

    def test_addVertices(self):
        g = Graph.Graph()
        vertices = [1, 2, 4, 7, 9]
        g.addVertices(vertices)
        self.assertEqual(g.getVertexCount(), len(vertices))
        self.assertDictEqual(g.adjDict, {
            1: [],
            2: [],
            4: [],
            7: [],
            9: []
        })

    def test_removeVertex(self):
        g = Graph.Graph()
        g.removeVertex(0)
        g.addVertices(range(1, 5))
        g.addEdge(1, 3)
        g.addEdge(2, 3)
        g.removeVertex(3)
        self.assertEqual(g.getVertexCount(), 3)
        self.assertDictEqual(g.adjDict, {
            1: [],
            2: [],
            4: []
        })

    def test_addEdge(self):
        g = Graph.Graph()
        g.addVertices(range(1, 6))
        g.addEdge(1, 2)
        self.assertEqual(g.getEdgeCount(), 1)
        g.addEdge(1, 2)  #
        self.assertEqual(g.getEdgeCount(), 1)
        g.addEdge(5, 5)  #
        self.assertEqual(g.getEdgeCount(), 1)
        g.addEdge(3, 3)  #
        self.assertEqual(g.getEdgeCount(), 1)
        g.addEdge(2, 3)
        self.assertEqual(g.getEdgeCount(), 2)
        g.addEdge(3, 2)  #
        self.assertEqual(g.getEdgeCount(), 2)
        g.addEdge(4, 2)
        self.assertEqual(g.getEdgeCount(), 3)
        g.addEdge(1, 2)  #
        self.assertEqual(g.getEdgeCount(), 3)

        self.assertDictEqual(g.adjDict, {
            1: [2],
            2: [1, 3, 4],
            3: [2],
            4: [2],
            5: []
        })

    def test_addEdges(self):
        g = Graph.Graph()
        g.addVertices(range(0, 5))
        edges = [[0, 2], [0, 4], [2, 3], [2, 4], [3, 4]]
        g.addEdges(edges)
        self.assertEqual(g.getEdgeCount(), len(edges))
        self.assertDictEqual(g.adjDict, {
            0: [2, 4],
            1: [],
            2: [0, 3, 4],
            3: [2, 4],
            4: [0, 2, 3]
        })

    def test_removeEdge(self):
        g = Graph.Graph()
        g.addVertices(range(0, 5))
        g.addEdge(0, 1)
        g.addEdge(1, 2)
        g.addEdge(2, 3)
        g.addEdge(3, 4)
        self.assertEqual(g.getVertexCount(), 5)
        self.assertEqual(g.getEdgeCount(), 4)
        g.removeEdge(3, 5)
        self.assertEqual(g.getVertexCount(), 5)
        self.assertEqual(g.getEdgeCount(), 4)
        g.removeEdge(3, 4)
        self.assertEqual(g.getEdgeCount(), 3)
        self.assertDictEqual(g.adjDict, {
            0: [1],
            1: [0, 2],
            2: [1, 3],
            3: [2],
            4: []
        })

    def test_getVertexCount(self):
        g = Graph.Graph()
        g.addVertices(range(0, 10))
        g.addEdge(1, 5)
        g.addEdge(3, 5)
        g.addEdge(2, 4)
        g.addEdge(1, 4)
        g.addEdge(3, 5)
        g.addEdge(2, 1)
        g.addEdge(3, 6)
        self.assertEqual(g.getVertexCount(), 10)

    def test_getEdgeCount(self):
        g = Graph.Graph()
        g.addVertices(range(0, 7))
        g.addEdge(1, 5)
        g.addEdge(3, 5)
        g.addEdge(2, 4)
        g.addEdge(1, 4)
        g.addEdge(3, 5)
        g.addEdge(2, 1)
        g.addEdge(3, 6)
        self.assertEqual(g.getEdgeCount(), int(sum([len(i) for _, i in g.adjDict.items()]) / 2))

    def test_areConnected(self):
        g = Graph.Graph()
        g.addVertices(range(0, 6))
        g.addEdge(2, 5)
        g.addEdge(2, 4)
        g.addEdge(1, 4)
        g.addEdge(1, 2)
        self.assertTrue(g.connected(2, 5))
        self.assertTrue(g.connected(1, 4))
        self.assertFalse(g.connected(1, 3))
