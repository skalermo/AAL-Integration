import argparse
import sys


from Algorithms import WelshPowell
from IOHandling import parseInput
from GraphGen import genGraph


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='Main.py', description='Program to color a graph')
    subparsers = parser.add_subparsers(dest='command', help='sub-command help')

    parser_m1 = subparsers.add_parser('m1', help='Color graph provided via stdin')

    parser_m2 = subparsers.add_parser('m2', help='Generate instance of the problem and solve it')
    parser_m2.add_argument('-n', type=int, metavar='', help='Number of vertices')
    parser_m2.add_argument('-d', type=float, metavar='', help='Density of the graph')
    parser_m2.add_argument('-k', type=int, metavar='', help='Make graph k-divisible')

    parser_m3 = subparsers.add_parser('m3', help='Perform the benchmark')
    parser_m3.add_argument('-n', type=int, metavar='', help='Number of vertices')
    parser_m3.add_argument('-d', type=float, metavar='', help='Density of the graph')
    # parser_m2.add_argument('-k', type=int, metavar='', help='Make graph k-divisible')
    parser_m3.add_argument('-K', type=int, metavar='', help='Problem count')
    parser_m3.add_argument('-s', '-step', type=int, metavar='', help='Generate problems\' sizes with this step')
    parser_m3.add_argument('-r', type=int, metavar='', help='Number of generated instances for each size')

    # Parsing arguments
    args = vars(parser.parse_args())

    # Handle m1 scenario
    if args['command'] == 'm1':
        graph = parseInput(sys.stdin)
        print(WelshPowell(graph))

    # Handle m2 scenario
    elif args['command'] == 'm2':
        n = args['n']
        d = args['d']
        k = args['k']
        graph = genGraph(n, d, k)
        print(WelshPowell(graph))

    # Handle m3 scenario
    elif args['command'] == 'm3':
        # todo
        pass

    # Wrong input, print help
    else:
        parser.print_help()



