import json
import sys
import io
import os


import Graph


def parseInput(inputToParse):
    g = Graph.Graph()
    g.setDict(json.load(inputToParse))
    return g


def dumpGraph(g):
    json.dump(g.getDict(), sys.stdout, indent=4, sort_keys=True)


def dumpTmpData(*args):
    with io.open('.results', 'a') as f:
        f.write(json.dumps(*args) + '\n')


def extractTmpData():
    filename = '.results'
    data = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            data.append(json.loads(line))
        return data


def removeTmpFile():
    filename = '.results'
    if os.path.isfile(filename):
        os.remove(filename)


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

    # row = (vertexCount, avg t(n), q(n), avg colorsUsed)
    for row in data:
        print(row[0], str(row[1])[:10], str(row[2])[:10], str(row[3])[:7], sep='|')
    print()

