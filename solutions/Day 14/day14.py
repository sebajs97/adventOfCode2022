# DAY 14: REGOLITH RESERVOIR

# LINK: https://adventofcode.com/2022/day/14

#### Funciones auxiliares
def format_data(data: list):
    minX = None
    maxX = None
    maxY = None
    salida = []
    for line in data:
        corners = line.split(' -> ')
        corners = [[int(coord) for coord in c.split(',')] for c in corners]
        salida.append(corners[:])
        currentMinX = min([c[0] for c in corners])
        currentMaxX = max([c[0] for c in corners])
        currentMaxY = max([c[1] for c in corners])
        if minX == None or currentMinX<minX:
            minX = currentMinX
        if maxX == None or currentMaxX>maxX:
            maxX = currentMaxX
        if maxY == None or currentMaxY>maxY:
            maxY = currentMaxY
    minX = 500 if minX>500 else minX
    return salida, [minX, maxX, maxY]
    
def create_map(data: list, limits: list):
    minX = limits[0]
    maxX = limits[1]
    maxY = limits[2]
    width = maxX-minX
    height = maxY
    mapa = [['.' for _ in range(width+1)] for _ in range(height+1)]
    for line in data:
        for i in range(len(line)-1):
            x1 = line[i][0] - minX
            y1 = line[i][1]
            x2 = line[i+1][0] - minX
            y2 = line[i+1][1]
            # xa es el menor, xb es el mayor, igual con las y
            xa = x1 if x1<x2 else x2
            xb = x1 if x1>x2 else x2
            ya = y1 if y1<y2 else y2
            yb = y1 if y1>y2 else y2

            for x in range(xa, xb+1):
                for y in range(ya, yb+1):
                    mapa[y][x] = '#'
    return mapa

def sand_fall(startPos, mapa, limits):
    fallsForever = False
    previousPos = None
    currentPos = startPos[:]
    while(previousPos!=currentPos):
        previousPos = currentPos[:]
        currentPos, fallsForever = one_step_fall(currentPos, mapa, limits)
        if (previousPos == currentPos):
            if fallsForever:
                mapa[currentPos[1]][currentPos[0]] = '.'
            break
        # Set new space as sand
        x = currentPos[0]
        y = currentPos[1]
        mapa[y][x] = 'o'
        # Restore previous space to air
        x = previousPos[0]
        y = previousPos[1]
        mapa[y][x] = '.'
    return mapa, fallsForever

def one_step_fall(cPos, mapa, limits):
    fallsForever = False
    x = cPos[0]
    y = cPos[1]

    if (x in [limits[0], limits[1]]) or (y == limits[2]):
        fallsForever = True
        return [x, y], fallsForever
    
    if mapa[y+1][x] == '.':
        newPos = [x, y+1]
    elif mapa[y+1][x-1] == '.':
        newPos = [x-1, y+1]
    elif mapa[y+1][x+1] == '.':
        newPos = [x+1, y+1]
    else:
        newPos = [x, y]
    return newPos, fallsForever
    
def create_map_2(data: list, limits: list):
    minX = limits[0]
    maxX = limits[1]
    maxY = limits[2]
    width = maxX-minX
    height = maxY
    mapa = [['.' for _ in range(width+1)] for _ in range(height+1)]
    for line in data:
        for i in range(len(line)-1):
            x1 = line[i][0] - minX
            y1 = line[i][1]
            x2 = line[i+1][0] - minX
            y2 = line[i+1][1]
            # xa es el menor, xb es el mayor, igual con las y
            xa = x1 if x1<x2 else x2
            xb = x1 if x1>x2 else x2
            ya = y1 if y1<y2 else y2
            yb = y1 if y1>y2 else y2

            for x in range(xa, xb+1):
                for y in range(ya, yb+1):
                    mapa[y][x] = '#'
        
        mapa[-1] = ['#' for pos in mapa[-1]]

    return mapa

def sand_fall_2(startPos, mapa, limits):
    previousPos = None
    currentPos = startPos[:]
    while(previousPos!=currentPos):
        previousPos = currentPos[:]
        currentPos = one_step_fall_2(currentPos, mapa, limits)
        if (previousPos == currentPos):
            if (currentPos==startPos):
                mapa[currentPos[1]][currentPos[0]] = 'o'
            break
        # Set new space as sand
        x = currentPos[0]
        y = currentPos[1]
        mapa[y][x] = 'o'
        # Restore previous space to air
        x = previousPos[0]
        y = previousPos[1]
        mapa[y][x] = '.'
    return mapa

def one_step_fall_2(cPos, mapa, limits):
    x = cPos[0]
    y = cPos[1]
    
    if mapa[y+1][x] == '.':
        newPos = [x, y+1]
    elif mapa[y+1][x-1] == '.':
        newPos = [x-1, y+1]
    elif mapa[y+1][x+1] == '.':
        newPos = [x+1, y+1]
    else:
        newPos = [x, y]
    return newPos

#### Problemas resueltos

def problem1(data: list):
    spawn = [500, 0]
    data, limits = format_data(data)
    # Ajustamos la escala X del spawn
    spawn[0] = spawn[0] - limits[0]
    mapa = create_map(data, limits)

    # Ajustamos la escala X de los limites para que empiecen desde cero
    limits[1] = limits[1] - limits[0]
    limits[0] = 0

    fallsForever = False
    sandCount = 0
    while(fallsForever == False):
        mapa, fallsForever = sand_fall(spawn, mapa, limits)
        if not fallsForever:
            sandCount += 1 
    print(sandCount)

def problem2(data: list):
    spawn = [500, 0]
    data, limits = format_data(data)
    limits[2] = limits[2] + 2
    limits[0] = limits[0] - limits[2]
    limits[1] = limits[1] + limits[2]

    # Ajustamos la escala X del spawn
    spawn[0] = spawn[0] - limits[0]
    mapa = create_map_2(data, limits)

    limits[1] = limits[1] - limits[0]
    limits[0] = 0

    sandCount = 0
    while(mapa[spawn[1]][spawn[0]] != 'o'):
        mapa = sand_fall_2(spawn, mapa, limits)
        sandCount += 1
    print(sandCount)


if __name__=='__main__':
    input = [line.removesuffix('\n') for line in open('solutions/Day 14/input14_1.txt', 'r').readlines()]
    problem1(input)
    problem2(input)