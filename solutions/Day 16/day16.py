# DAY 16: PROBOSCIDEA VOLCANIUM

# LINK: https://adventofcode.com/2022/day/16

import re

### FUNCIONES AUXILIARES
def format_data(input: list):
    data = {}
    for line in input:
        rePattern = r'Valve (\w+) .+ rate=(\d+); .+ valves* (.+)'
        match = re.match(rePattern, line).groups()
        name = match[0]
        data[name] = {}
        data[name]['fr'] = int(match[1])
        data[name]['conn'] = match[2].split(', ')
        data[name]['valveOpen'] = 0
    return data

def find_optimal_path(graph: list, start: str) -> list:
    # Devuelve una lista (óptima) con los puntos visitados

    # TODO: setup initial values
    # TODO: excecute recursive algorithm
    pass

def recursive_algorithm(g, t, cPos, graph, unvisited):
    getClosedValves = [name for name, val in graph if  val['valveOpen']==0]
    # get all neighboors
    neighboors = graph[cPos]['conn']
    # TODO: estimate heuristic
    # TODO: excecute for new most likely optimal point
    # TODO: return if 30 min mark reached
    pass

def estimate_best_outcome(graph, unvisited):
    pass

### RESOLUCIÓN DE PROBLEMAS

def problem1(input: list):
    graph = format_data(input)
    listaPuntos = find_optimal_path(graph, 'AA')

def problem2(input: list):
    pass

if __name__=='__main__':
    input = [line.removesuffix('\n') for line in open('solutions/Day 16/input16_1.txt', 'r').readlines()]
    problem1(input)