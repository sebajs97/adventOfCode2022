# DAY 8: TREETOP TREE HOUSE

# LINK: https://adventofcode.com/2022/day/8

def check_if_max(txt, val, max, visibles):
    if (val > max):
        if (txt not in visibles):
            visibles.append(txt)
        max = val
    return max, visibles

def check_visible_from_left_or_right(input: list, visibles: list, side: str):
    for y in range(len(input)):
        if side=='l': # ESTA LINEA DE CODIGO DEBE ESTAR AQUI PARA QUE REVERSED NO SE RESETEE
            rango = range(len(input[0]))
        elif side == 'r':
            rango = reversed(range(len(input[0])))
        max = -1
        for x in rango:
            val = input[y][x]
            txt = f'{x},{y}'
            max, visibles = check_if_max(txt, val, max, visibles)
    return visibles

def check_visible_from_top_or_bottom(input: list, visibles: list, side: str):
    for x in range(len(input[0])):
        if side == 't': # ESTA LINEA DE CODIGO DEBE ESTAR AQUI PARA QUE REVERSED NO SE RESETEE
            rango = range(len(input))
        elif side == 'b':
            rango = reversed(range(len(input)))
        max = -1
        for y in rango:
            if x==3 and y == 3:
                pass
            val = input[y][x]
            txt = f'{x},{y}'
            max, visibles = check_if_max(txt, val, max, visibles)
    return visibles

def problem1(input: list):
    visibles = []
    visibles = check_visible_from_left_or_right(input, visibles, 'l')
    visibles = check_visible_from_left_or_right(input, visibles, 'r')
    visibles = check_visible_from_top_or_bottom(input, visibles, 't')
    visibles = check_visible_from_top_or_bottom(input, visibles, 'b')
    print(len(visibles))

def count_views_up_or_down(input: list, x: int, y: int, mode: str):
    if mode == 'u':
        rango = range(y-1, -1, -1)
    elif mode == 'd':
        rango = range(y+1, len(input))

    counter = 0
    for newY in rango:
        value = input[y][x]
        compareValue = input[newY][x]
        counter += 1
        if (value <= compareValue):
            break
    return counter

def count_views_left_or_right(input: list, x: int, y: int, mode: str):
    if mode == 'l':
        rango = range(x-1, -1, -1)
    elif mode == 'r':
        rango = range(x+1, len(input))

    counter = 0
    for newX in rango:
        value = input[y][x]
        compareValue = input[y][newX]
        counter += 1
        if (value <= compareValue):
            break
    return counter

def problem2(input: list):
    width = len(input[0])
    height = len(input)

    maxViews = 0
    for y in range(height):
        for x in range(width):
            up = count_views_up_or_down(input, x, y, 'u')
            left = count_views_left_or_right(input, x, y, 'l')
            down = count_views_up_or_down(input, x, y, 'd')
            right = count_views_left_or_right(input, x, y, 'r')
            totalScore = up*left*down*right
            maxViews = totalScore if totalScore>maxViews else maxViews

    print(maxViews)

if __name__=='__main__':
    input = [line.removesuffix('\n') for line in open('solutions/Day 8/input8_1.txt', 'r').readlines()]
    input = [[int(val) for val in line] for line in input]
    problem1(input)
    problem2(input)
