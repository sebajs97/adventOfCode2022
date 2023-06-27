# DAY 9: ROPE BRIDGE

# LINK: https://adventofcode.com/2022/day/9

from math import sqrt

def move_head(headCoords: list, move: list, tailCoords: list, tailHist: list):
    dir = move[0]
    for i in range(move[1]):
        if dir=='R':
            headCoords[0] += 1
        elif dir=='L':
            headCoords[0] -= 1
        if dir=='U':
            headCoords[1] += 1
        elif dir=='D':
            headCoords[1] -= 1
        tailCoords = move_tail(headCoords, tailCoords, dir)
        tailHist.append(tailCoords[:])
    return headCoords, tailCoords, tailHist

def move_head2(headCoords: list, dir: list,):
    if dir=='R':
        headCoords[0] += 1
    elif dir=='L':
        headCoords[0] -= 1
    if dir=='U':
        headCoords[1] += 1
    elif dir=='D':
        headCoords[1] -= 1
    return headCoords


def put_tail_next_to_head(headCoords: list, tailCoords: list):

    diff = [headCoords[0] - tailCoords[0], headCoords[1] - tailCoords[1]]
    for i, d in enumerate(diff):
        if d > 0:
            tailCoords[i] += 1
        elif d < 0:
            tailCoords[i] -= 1
    return tailCoords


def move_tail(headCoords:list, tailCoords: list, dir: str):
    xh = headCoords[0]
    yh = headCoords[1]
    xt = tailCoords[0]
    yt = tailCoords[1]
    c = sqrt(pow(xh-xt,2)+pow(yh-yt,2))
    if c<2:
        return tailCoords
    tailCoords = put_tail_next_to_head(headCoords, tailCoords)
    return tailCoords

def get_unique_positions(tailHist: list):
    uniqueHist = []
    for item in tailHist:
        if item not in uniqueHist:
            uniqueHist.append(item)
    return uniqueHist

def move_all_knots(move: list, coords: list, tailHist: list):
    dir = move[0]
    qtyOfRepeats = move[1]
    
    # Ciclo para cada rep en una misma dirección
    for _ in range(qtyOfRepeats):
        coords[0] = move_head2(coords[0], dir)
        for i in range(1, len(coords)):
            coords[i] = move_tail(coords[i-1], coords[i], dir)
        tailHist.append(coords[-1][:])
    a = print_matrix(coords)
    return coords, tailHist

def print_matrix(coords:list):
    exs = [c[0] for c in coords]
    wyes = [c[1] for c in coords]
    maxX = max(exs)+3
    maxY = max(wyes)+3
    minX = min(exs)-2
    minY = min(wyes)-2
    txtStr = [['.' for _ in range(minX, maxX)] for line in range(minY, maxY)]
    for i, c in enumerate(coords):
        relativeX = c[0]-minX
        relativeY = (maxY-minY-1)-(c[1]-minY)
        if txtStr[relativeY][relativeX] == '.':
            txtStr[relativeY][relativeX] = str(i)
    txtStr = [''.join(line) for line in txtStr]
    txtStr = [f"{maxY-1-i:<5}{l}" for  i, l in enumerate(txtStr)]
    return txtStr

### RESOLUCIÓN DE LOS PROBLEMAS

def problem1(input: list):
    headCoords = [0, 0]
    tailCoords = [0, 0]
    tailHist = [tailCoords[:]]

    for line in input:
        headCoords, tailCoords, tailHist = move_head(headCoords, line, tailCoords, tailHist)
    
    uniqueHist = get_unique_positions(tailHist)

    result = len(uniqueHist)
    print(result)

def problem2(input: list):
    coords = [[0, 0] for _ in range(10)] # Son 10 puntos en total
    tailHist = [[0,0]]

    # Ciclo para cada linea de código
    for line in input:
        coords, tailHist = move_all_knots(line, coords, tailHist)

    # Obtener las posiciones no repetidas
    uniqueHist = get_unique_positions(tailHist)

    result = len(uniqueHist)
    print(result)


if __name__=='__main__':
    input = [line.removesuffix('\n') for line in open('solutions/Day 9/input9_1.txt', 'r').readlines()]
    input = [(lambda x: [x[0], int(x[1])])(line.split(' ')) for line in input]
    problem1(input)
    problem2(input)