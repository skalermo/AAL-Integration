import json
import sys


import Graph


def parseInput(inputToParse):
    g = Graph.Graph()
    g.__dict__ = json.load(inputToParse)
    return g


def dump(g):
    json.dump(g.__dict__, sys.stdout, indent=4, sort_keys=True)

