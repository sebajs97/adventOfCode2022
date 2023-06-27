
def is_visible_up(input, x, y, visibles={}):
    xyTXT = f'{x},{y}'
    if xyTXT in visibles:
        return visibles[xyTXT], visibles
    if y==0:
        return True, visibles

    value = input[y][x]
    
    if (input[y-1][x] >= input[y][x]): # Si es mas bajo que el anterior
        isVisible = False
    else: # Si es mas alto que el anterior
        isVisibleUp, visibles = is_visible_up(input, x, y-1, visibles)
        if isVisibleUp:
            isVisible = True
        else:
            inFront = input[:y][:]
            inFront = [l[x] for l in inFront]
            isVisible = max(inFront) < value

    visibles[xyTXT] = isVisible
    return isVisible, visibles

def is_visible_down(input, x, y, visibles={}):
    xyTXT = f'{x},{y}'
    if xyTXT in visibles:
        return visibles[xyTXT], visibles
    if y==len(input)-1:
        return True, visibles

    value = input[y][x]

    if (input[y+1][x] >= value): # Si es mas bajo que el siguiente
        isVisible = False
    else: # Si es mas alto que el anterior
        isVisibleDown, visibles = is_visible_down(input, x, y+1, visibles)
        if isVisibleDown:
            isVisible = True
        else:
            inFront = input[y+1:][:]
            inFront = [l[x] for l in inFront]
            isVisible = max(inFront) < value
    
    visibles[xyTXT] = isVisible
    return isVisible, visibles

def is_visible_left(input, x, y, visibles={}):
    xyTXT = f'{x},{y}'
    if xyTXT in visibles:
        return visibles[xyTXT], visibles
    if x==0:
        return True, visibles

    value = input[y][x]
    
    if (input[y][x-1] >= input[y][x]): # Si es mas bajo que el anterior
        isVisible = False
    else: # Si es mas alto que el anterior
        isVisibleLeft, visibles = is_visible_left(input, x-1, y, visibles)
        if isVisibleLeft:
            isVisible = True
        else:
            inFront = input[y][:x]
            isVisible = max(inFront) < value
    visibles[xyTXT] = isVisible
    return isVisible, visibles

def is_visible_right(input, x, y, visibles={}):
    xyTXT = f'{x},{y}'
    if xyTXT in visibles:
        return visibles[xyTXT], visibles
    if x==len(input[0])-1:
        return True, visibles

    value = input[y][x]
    
    if (input[y][x+1] >= input[y][x]): # Si es mas bajo que el anterior
        isVisible = False
    else: # Si es mas alto que el anterior
        isVisibleRight, visibles = is_visible_right(input, x+1, y, visibles)
        if isVisibleRight:
            isVisible = True
        else:
            inFront = input[y][x+1:]
            isVisible = max(inFront) < value    

    visibles[xyTXT] = isVisible
    return isVisible, visibles

def check_if_visible_from_any_side(input, x, y, visiblesWholeDict: dict):
    thisIsVisible = False
    thisIsVisible, visiblesWholeDict['down'] = is_visible_down(input, x, y, visiblesWholeDict['down'])
    if thisIsVisible: return True
    thisIsVisible, visiblesWholeDict['up'] = is_visible_up(input, x, y, visiblesWholeDict['up'])
    if thisIsVisible: return True
    thisIsVisible, visiblesWholeDict['left'] = is_visible_left(input, x, y, visiblesWholeDict['left'])
    if thisIsVisible: return True
    thisIsVisible, visiblesWholeDict['right'] = is_visible_right(input, x, y, visiblesWholeDict['right'])
    if thisIsVisible: return True 
    return False


def problem1(input: list):
    visiblesWholeDict = {'up': {}, 'down': {}, 'left': {}, 'right': {}}
    areVisibles = []
    for y in range(len(input)):
        for x in range(len(input[0])):
            if check_if_visible_from_any_side(input, x, y, visiblesWholeDict):
                areVisibles.append(f'{x},{y}')
    print(len(areVisibles))

def problem2(input: list):
    pass

if __name__=='__main__':
    input = [line.removesuffix('\n') for line in open('solutions/Day 8/input8_1.txt', 'r').readlines()]
    input = [[int(val) for val in line] for line in input]
    problem1(input)
