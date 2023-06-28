# DAY 12: HILL CLIMBING ALGORITHM

# LINK: https://adventofcode.com/2022/day/12

### Clases

class Position():
    def __init__(self, coords: list, height: int,  visited = False,):
        # Clase Posición que guarda la altura, coordenadas, estado (visitado o no) y el costo de llegar a este punto
        self.x = coords[0]
        self.y = coords[1]
        self.height = height
        self.visited = visited
        self.cost = 999999999999

### FUNCIONES AUXILIARES

def format_input(input: list):
    # Crea las posiciones en una lista de listas. La altura la define la letra (a=0, b=1, c=2..)
    # retorna la lista de listas, el punto de inicio y el punto final
    output = []
    for j in range(len(input)):
        output.append([])
        for i in range(len(input[0])):
            char = input[j][i]
            height = ord(char)-97
            if char == 'S':
                char = 'a'
                start = True
                height = ord(char)-97
                startPoint = Position([i, j], height)
            elif char == 'E':
                char = 'z'
                height = ord(char)-97
                end = Position([i, j], height)
            output[j].append(Position([i, j], height))
    return output, startPoint, end

def find_shortest_path(datos: list, startPoint: Position, end: list) -> int:
    datos[startPoint.y][startPoint.x].cost = 0
    while (not datos[end.y][end.x].visited) and (len(get_unvisited(datos))>=0):
        unvisited = get_unvisited(datos)
        currentPosition = extract_min_from_unvisited(unvisited)
        morePaths = check_if_there_are_no_more_paths(unvisited)
        if not morePaths:
            break

        x = currentPosition.x
        y = currentPosition.y
        ## Revisar vecinos
        # Arriba
        if y > 0:
            if (datos[y-1][x].height <= currentPosition.height+1) and not datos[y-1][x].visited:
                if datos[y-1][x].cost > currentPosition.cost + 1:
                    datos[y-1][x].cost = currentPosition.cost + 1
        # Abajo
        if y < len(datos) - 1:
            if datos[y+1][x].height<=currentPosition.height+1 and not datos[y+1][x].visited:
                if datos[y+1][x].cost > currentPosition.cost + 1:
                    datos[y+1][x].cost = currentPosition.cost + 1
        
        # Izquierda
        if x > 0:
            if datos[y][x-1].height<=currentPosition.height+1 and not datos[y][x-1].visited:
                if datos[y][x-1].cost > currentPosition.cost+1:
                    datos[y][x-1].cost = currentPosition.cost+1
        
        # Derecha
        if x < len(datos[0]) - 1:
            if datos[y][x+1].height <= currentPosition.height+1 and not datos[y][x+1].visited:
                if datos[y][x+1].cost > currentPosition.cost+1:
                    datos[y][x+1].cost = currentPosition.cost+1

        datos[currentPosition.y][currentPosition.x].visited = True
    return datos[end.y][end.x].cost
    
def get_unvisited(datos: list):
    unvisited = []
    for fila in datos:
        for position in fila:
            if not position.visited:
                unvisited.append(position)
    return unvisited

def extract_min_from_unvisited(unvisited: list):
    minPosition = 0
    for i in range(len(unvisited)):
        if unvisited[i].cost < unvisited[minPosition].cost:
            minPosition = i
    return unvisited[minPosition]

def get_starting_points(datos: list)-> list:
    startingPoints = []
    for line in datos:
        for point in line:
            if point.height == 0:
                startingPoints.append((point))
    return startingPoints

def check_if_there_are_no_more_paths(unvisited:list):
    costs = [p.cost for p in unvisited if p.cost != 999999999999]
    if len(costs) != 0:
        return True
    return False


#### RESOLUCION DE PROBLEMAS

def problem1(input: list):
    datos, start, end = format_input(input)
    shortestPath = find_shortest_path(datos, start, end)
    print(shortestPath)

def problem2(input: list):
    datos, _, end = format_input(input)
    startingPoints = get_starting_points(datos)
    pathLengths = []
    for startingPoint in startingPoints:
        datos, _, end = format_input(input)
        pathLengths.append(find_shortest_path(datos, startingPoint, end))
    print(min(pathLengths))

if __name__=='__main__':
    input = [line.removesuffix('\n') for line in open('solutions/Day 12/input12_1.txt', 'r').readlines()]
    problem1(input)
    problem2(input)