from unittest import TestCase
from GraphGen import genEdges, genGraph
from Algorithms import bruteForce


class TestGraphGen(TestCase):
    def test_genEdges(self):
        n = 100
        density = 0.8
        edgesCount = int(n*(n-1)/2*density)
        edges = genEdges(n, density)
        self.assertEqual(edgesCount, len(edges))

    def test_genGraph(self):
        n = 100
        density = 0.8
        edgesCount = int(n * (n - 1) / 2 * density)
        g = genGraph(n, density)
        self.assertEqual(n, g.getVertexCount())
        self.assertEqual(edgesCount, g.getEdgeCount())

    def test_genGraphWithGroups(self):
        n = 10
        density = 0.8
        i = 8
        for groupsCount in range(1, i+1):
            g = genGraph(n, density, groupsCount)
            chromatic = bruteForce(g, True)[1]
            print(groupsCount, chromatic)
            self.assertTrue(groupsCount >= chromatic)
