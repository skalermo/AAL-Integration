import json
import sys


import Graph


def parseInput(inputToParse):
    g = Graph.Graph()
    g.setdict(json.load(inputToParse))
    return g


def dump(g):
    json.dump(g.getdict(), sys.stdout, indent=4, sort_keys=True)


def outputBenchmarkResults(info, data):
    functionName, vertexNumber, density, divisibility, problemCount, step, instanceCount = info

    print(functionName + ' n=' + str(vertexNumber) + ', ' + str(vertexNumber + step) + ',... -> '
          + str(vertexNumber + (problemCount-1)*step) + ' d=' + str(density), end='')
    if divisibility:
        print(' k=' + str(divisibility), end='')
    print(' r=' + str(instanceCount))
    print('\n')

    print("n", "t(n)[ms]", "q(n)", "colors used", sep='|')
    print("---", "---", "---", ":---:", sep='|')

    for row in data:
        print(*row, sep='|')
    print()

