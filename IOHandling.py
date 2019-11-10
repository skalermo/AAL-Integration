import json
import sys


import Graph


def parseInput(inputToParse):
    g = Graph.Graph()
    g.setdict(json.load(inputToParse))
    return g


def dump(g):
    json.dump(g.getdict(), sys.stdout, indent=4, sort_keys=True)

