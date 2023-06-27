# DAY 15: BEACON EXCLUSION ZONE

# LINK: https://adventofcode.com/2022/day/15

### FUNCIONES AUXILIARES

def format_input(input: list):
    sensors = []
    beacons = []
    for line in input:
        lineSplit = line.split('x=')
        sensorPos = lineSplit[1].split(':')[0]
        beaconPos = lineSplit[2]
        sensorPos = [int(p) for p in sensorPos.split(', y=')]
        beaconPos = [int(p) for p in beaconPos.split(', y=')]
        sensors.append(sensorPos[:])
        beacons.append(beaconPos[:])
    return sensors, beacons

def get_distances(sensors, beacons):
    distances = []
    for i in range(len(sensors)):
        distance = find_manh_distance(sensors[i], beacons[i])
        distances.append(distance)
    return distances

def find_manh_distance(p1, p2):
    distance = 0
    distance += abs(p1[0] - p2[0])
    distance += abs(p1[1] - p2[1])
    return distance

def get_all_covered_points(sensors, distances, y):
    coveredPointsXRanges = []
    for i in range(len(sensors)):
        xSens = sensors[i][0]
        ySens = sensors[i][1]
        yLeftOver = distances[i] - abs(ySens-y)
        if yLeftOver>0:
            minCovered = xSens - yLeftOver
            maxCovered = xSens + yLeftOver
            coveredPointsXRanges = save_to_ranges(coveredPointsXRanges, minCovered, maxCovered)
    return coveredPointsXRanges

def save_to_ranges(coveredPointsXRanges: list, minCovered:int, maxCovered:int):
    isCovered = False
    for i in range(len(coveredPointsXRanges)):
        r = coveredPointsXRanges[i]
        start = r.start
        stop = r.stop
        if (minCovered>=start and maxCovered<=stop):
            isCovered = True
            break
        elif (minCovered<=start and maxCovered>=stop):
            coveredPointsXRanges[i] = range(minCovered, maxCovered+1)
            break
        elif (minCovered>stop or maxCovered<start):
            continue
        elif (maxCovered<=stop):
            isCovered = True
            coveredPointsXRanges[i] = range(minCovered, stop)
            break
        elif (minCovered>=start):
            isCovered = True
            coveredPointsXRanges[i] = range(start, maxCovered+1)
            break
        else:
            print('ERROR EN RANGOS')
    if not isCovered:
        coveredPointsXRanges.append(range(minCovered, maxCovered+1))
    return coveredPointsXRanges

def make_set_from_ranges(ranges:list):
    newSet = set()
    for r in ranges:
        newSet.update(r)
    return newSet

def discard_positions_already_occupied(sensors, beacons, y, coveredPoints:list):
    for pos in sensors+beacons:
        if pos[1] == y:
            if pos[0] in coveredPoints:
                coveredPoints.remove(pos[0])
    return coveredPoints


def get_lnFns(x, y, manh):
    fns = []
    fns.append({'fn':[1, y - x + (manh+1)], 'xLimits':[x-(manh+1), x]}) # NO
    fns.append({'fn':[1, y - x - (manh+1)], 'xLimits':[x, x+(manh+1)]}) # SE
    fns.append({'fn':[-1, y + x + (manh+1)], 'xLimits':[x, x+(manh+1)]}) # NE
    fns.append({'fn':[-1, y + x - (manh+1)], 'xLimits':[x-(manh+1), x]}) # SO
    return fns

def get_intersecions(fn1, fn2):
    intersections = None
    m1, b1 = fn1['fn']
    m2, b2 = fn2['fn']
    lims1 = fn1['xLimits']
    lims2 = fn2['xLimits']
    rng1 = range(lims1[0], lims1[1]+1)
    rng2 = range(lims2[0], lims2[1]+1)
    if m1-m2!= 0:
        xIntersects = (b2-b1)/(m1-m2)
        # Si la intersección no es en un entero
        if xIntersects != int(xIntersects): 
            return None
        # Si está dentro del rango en el que aparece la función
        if (xIntersects >= lims1[0] and xIntersects<=lims1[1]) and (xIntersects >= lims2[0] and xIntersects<=lims2[1]):
            yIntersects = (m1 * xIntersects) + b1
            intersections = [xIntersects, yIntersects]
    return intersections


### RESOLUCIÓN DE PROBLEMA

def problem1(input: list):
    sensors, beacons = format_input(input)
    distances = get_distances(sensors, beacons)
    y = 2000000
    coveredPointsXCoords = get_all_covered_points(sensors, distances, y)
    coveredPointsSet = make_set_from_ranges(coveredPointsXCoords)
    coveredPointsSet = discard_positions_already_occupied(sensors, beacons, y, coveredPointsSet)
    result = len(coveredPointsSet)
    print(result)
    d = 5

def problem2(input:list):
    sensors, beacons = format_input(input)
    distances = get_distances(sensors, beacons)
    fns = []
    limitXY = 4000000 # Tamaño máximo donde se puede encontrar el punto

    # *Obtener las funciones que delimitan cada punto*
    # Las funciones obtendrán las 4 ecuaciones que contienen los puntos que rodean
    #  al los Sensores y su "zona segura", donde no puede haber más Beacons.
    # Si en el rango indicado solo hay un punto que no se encuentra dentro de una zona 
    #  segura, este punto TIENE que ser en la intersección de dos de las funciones 
    #  explicadas arriba.

    # -3 ..........*.................
    # -2 .........*#*................
    # -1 ........*###*...............
    #  0 ....S..*#####*..............
    #  1 ......*#######*.......S.....
    #  2 .....*#########S............
    #  3 ....*###########SB..........
    #  4 ...*#############*..........
    #  5 ..*###############*.........
    #  6 .*#################*........
    #  7 *#########S#######S#*.......
    #  8 .*#################*........
    #  9 ..*###############*.........
    # 10 ....B############*..........
    # 11 ..S.*###########*...........
    # 12 .....*#########*............
    # 13 ......*#######*.............
    # 14 .......*#####*S.......S.....
    # 15 B.......*###*...............
    # 16 .........*#*................
    # 17 ..........*.....S..........

    for i in range(len(sensors)):
        x = sensors[i][0]
        y = sensors[i][1]
        currentFns = get_lnFns(x, y, distances[i])
        fns.extend(currentFns)
    
    # Verificamos cuáles son los puntos con interseccones
    intersections = []
    for i in range(len(fns)):
        for j in range(len(fns)):
            intersection = get_intersecions(fns[i], fns[j])
            if intersection != None and intersection not in intersections:
                if intersection[0] <= limitXY and intersection[0] >= 0 and intersection[1] <= limitXY and intersection[1] >= 0:
                    intersections.append(intersection)

    # Para cada punto, probar que esté a más de la distancia manhattan
    #  de todos los sensores
    validIntersections = []
    for inter in intersections:
        valid = True
        for i in range(len(sensors)):
            if find_manh_distance(sensors[i], inter) <= distances[i]:
                valid = False
                break
        if valid:
            validIntersections.append(inter[:])


    # Calcular resultado final
    x = validIntersections[0][0]
    y = validIntersections[0][1]
    result = (4000000 * x) + y
    print(result)

if __name__=='__main__':
    input = [line.removesuffix('\n') for line in open('solutions/Day 15/input15_1.txt', 'r').readlines()]
    problem1(input)
    problem2(input)