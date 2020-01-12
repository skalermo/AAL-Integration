import argparse
import sys


from Algorithms import WelshPowell, bruteForceWithHeuristics
from IOHandling import parseInput
from GraphGen import genGraph
from Benchmark import testit


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='Main.py', description='Program to color a graph')
    subparsers = parser.add_subparsers(dest='scenario', help='sub-command help')

    parser_m1 = subparsers.add_parser('m1', help='Color graph provided via stdin')

    parser_m2 = subparsers.add_parser('m2', help='Generate instance of the problem and solve it')
    parser_m2.add_argument('-n', type=int, metavar='', help='Number of vertices')
    parser_m2.add_argument('-d', type=float, metavar='', help='Density of the graph')
    parser_m2.add_argument('-k', type=int, metavar='', help='Make graph k-divisible')

    parser_m3 = subparsers.add_parser('m3', help='Perform the benchmark')
    parser_m3.add_argument('-w', action='store_true', help='Use Welsh-Powell algorithm')
    parser_m3.add_argument('-b', action='store_true', help='Use Brute force algorithm with heuristics')

    parser_m3.add_argument('-n', type=int, metavar='', help='Number of vertices')
    parser_m3.add_argument('-d', type=float, metavar='', help='Density of the graph')
    parser_m3.add_argument('-k', type=int, metavar='', help='Make graph k-divisible')
    parser_m3.add_argument('-c', type=int, metavar='', help='Problem count')
    parser_m3.add_argument('-s', '-step', type=int, metavar='', help='Generate problems\' sizes with this step')
    parser_m3.add_argument('-r', type=int, metavar='', help='Number of generated instances for each size')
    parser_m3.add_argument('-f', action='store_true', default=False, help='Use temporary file to store results')

    # Parsing arguments
    args = vars(parser.parse_args())

    # Handle m1 scenario
    if args['scenario'] == 'm1':
        graph = parseInput(sys.stdin)
        print(WelshPowell(graph))

    # Handle m2 scenario
    elif args['scenario'] == 'm2':
        vertexNumber = args['n']
        density = args['d']
        divisibility = args['k']
        graph = genGraph(vertexNumber, density, divisibility)
        print(WelshPowell(graph))

    # Handle m3 scenario
    elif args['scenario'] == 'm3':
        fun = None
        if args['w']:
            fun = WelshPowell
        elif args['b']:
            fun = bruteForceWithHeuristics
        else:
            parser_m3.print_help()
            exit(1)

        vertexNumber = args['n']
        density = args['d']
        divisibility = args['k']
        problemCount = args['c']
        step = args['s']
        instanceCount = args['r']
        useTmpfile = args['f']
        testit(fun, (vertexNumber, density, divisibility, problemCount, step, instanceCount, useTmpfile))

    # Wrong input, print help
    else:
        parser.print_help()



