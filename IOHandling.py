import json
import sys
import io
import os


import Graph


def parseInput(inputToParse):
    """
    Parse json-formatted input
    :param inputToParse: standard input
    :return: Generated graph
    """
    g = Graph.Graph()
    g.setDict(json.load(inputToParse))
    return g


def dumpGraph(g):
    """
    Write graph to stdout using json notation
    :param g: Input graph
    """
    json.dump(g.getDict(), sys.stdout, indent=4, sort_keys=True)


def dumpTmpData(*args):
    """
    Saves processed data from yet not finished task into .results file
    :param args: Processed data (used algorithm and running parameters, number of vertices and edges, execution time, number of colors used)
    """
    with io.open('.results', 'a') as f:
        f.write(json.dumps(*args) + '\n')


def extractTmpData():
    """
    Receive data of last benchmark results from the temporary file
    :return: Received data
    """
    filename = '.results'
    data = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            data.append(json.loads(line))
        return data


def removeTmpFile():
    """
    Delete temporary file

    """
    filename = '.results'
    if os.path.isfile(filename):
        os.remove(filename)


def outputBenchmarkResults(info, data):
    """
    Print formatted in markdown notation benchmark results
    :param info: Details of benchmark (algorithm, size of graphs to process etc)
    :param data: number of vertices, execution times, calculated q-values, numbers of colors used

    """
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

