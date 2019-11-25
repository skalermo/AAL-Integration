import time
from GraphGen import genGraph
from Algorithms import WelshPowell
from IOHandling import outputBenchmarkResults, removeTmpFile, dumpTmpData, extractTmpData


"""Functions for testing algorithms complexity"""


def timing(f, *args):
    time1 = time.time()
    _, colorsUsed = f(*args)
    time2 = time.time()
    return colorsUsed, time2 - time1


def testit(f, arguments):

    vertexNumber, density, divisibility, problemCount, step, instanceCount, useTmpfile = arguments

    infoToOutput = (f.__name__, vertexNumber, density, divisibility, problemCount, step, instanceCount)

    if useTmpfile:
        removeTmpFile()
        dumpTmpData((f.__name__, vertexNumber, density, divisibility, problemCount, step, instanceCount))

    data = []
    # data = [[vertexNumber, measuredTime, q(n), colorOveruse], ...]

    # warming up
    WelshPowell(genGraph(1000, 0.75, 5))

    for i in range(problemCount):
        data.append([])
        timeSum = 0.0
        edgeCount = 0
        colorsUsedSum = 0.0

        for _ in range(instanceCount):
            g = genGraph(vertexNumber+step*i, density, divisibility)
            edgeCount = g.getEdgeCount()
            colorsUsed, timeSpent = timing(f, g)
            colorsUsedSum += colorsUsed
            timeSum += timeSpent

        colorsUsedAvg = colorsUsedSum / instanceCount
        timeAvg = timeSum / instanceCount

        data[i].append(vertexNumber+step*i)
        data[i].append(timeAvg)
        data[i].append(edgeCount)
        data[i].append(colorsUsedAvg)

        if useTmpfile:
            dumpTmpData(data[i])

    tmedian, Tmedian = calcMedian(f.__name__, data)

    calcQ(f.__name__, data, tmedian, Tmedian)

    outputBenchmarkResults(infoToOutput, data)


def wComplexity(n):
    """Theoretical complexity of WelshPowell algorithm"""

    return n**2


def bComplexity(n, e):
    """Theoretical complexity of Brute Force algorithm"""

    sum = 0
    for i in range(1, n+1):
        sum += i**n
    return sum * e


def blComplexity(n, s, e):
    """Theoretical complexity of Brute Force algorithm with heuristics"""

    return s**n*e + 1.44**n


def calcMedian(algorithm, data):
    median = len(data) // 2
    tmedian = data[median][1]
    Tmedian = 0.0

    if algorithm == 'WelshPowell':
        Tmedian = wComplexity(data[median][0])
    elif algorithm == 'bruteForce':
        Tmedian = bComplexity(data[median][0], data[median][2])
    elif algorithm == 'bruteForceWithHeuristics':
        Tmedian = blComplexity(data[median][0], data[median][3], data[median][2])

    return tmedian, Tmedian


def calcQ(algorithm, data, tmedian, Tmedian):
    complexity = 0.0
    for row in data:
        if algorithm == 'WelshPowell':
            complexity = wComplexity(row[0])
        elif algorithm == 'bruteForce':
            complexity = bComplexity(row[0], row[2])
        elif algorithm == 'bruteForceWithHeuristics':
            complexity = blComplexity(row[0], row[3], row[2])
        q = row[1] * Tmedian / complexity / tmedian

        # seconds to ms
        row[1] = row[1] * 1000

        row[2] = q


if __name__ == '__main__':
    data = extractTmpData()
    info = data[0]
    algorithm = info[0]
    data = data[1:]
    tmedian, Tmedian = calcMedian(algorithm, data)
    calcQ(algorithm, data, tmedian, Tmedian)
    outputBenchmarkResults(info, data)
