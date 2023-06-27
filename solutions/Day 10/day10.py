# DAY 10: CATHODE-RAY TUBE

# LINK: https://adventofcode.com/2022/day/10

#### FUNCIONES AUXILIARES

def read_instruction(line: str, cycle: int, toAdd:list):
    buffering = 0
    if line!='noop':
        number = int(line[5:])
        buffering = 1
        toAdd.append([cycle+2, number])
    return buffering, toAdd

def execute_cycle_logic(cycle, currentLine, buffering, hist, toAdd, x, input):
    continueCycle = True
    if buffering != 0: # Si está en buffering áun, pasar al siguiente ciclo
        buffering -= 1
        hist.append(x)
    else:
        # Si hay algo en cola y este es su turno (que debe serlo), sumarlo
        if len(toAdd)>0:
            if toAdd[0][0] == cycle:
                x += toAdd[0][1]
                toAdd.pop(0)
        hist.append(x)
        if (currentLine >= len(input) and len(toAdd)==0): # Si ya llegamos a la última línea -> salir
            continueCycle = False
        else:
            buffering, toAdd = read_instruction(input[currentLine], cycle, toAdd)
            currentLine += 1
    return currentLine, buffering, hist, toAdd, x, continueCycle

def check_if_draws(currentCycle, currentSpritePos)-> str:
    spritePositions = range(currentSpritePos-1, currentSpritePos+2)
    while currentCycle>40:
        currentCycle -= 40

    if currentCycle-1 in spritePositions:
        return '#'
    return '.'

#### RESOLUCIÓN DE PROBLEMAS

def problem1(input: list):
    x = 1
    cycle = 0
    buffering = 0
    currentLine = 0
    toAdd = []
    hist = []
    continueCycle = True
    while continueCycle:
        cycle += 1 # Aumentamos en 1 el ciclo
        currentLine, buffering, hist, toAdd, x, continueCycle = execute_cycle_logic(cycle, currentLine, buffering, hist, toAdd, x, input)
    result = 0
    for i in [20, 60, 100, 140, 180, 220]:
        val = (i*hist[i-1])
        result += val
    print(result)
                
def problem2(input: list):
    x = 1
    cycle = 0
    buffering = 0
    currentLine = 0
    toAdd = []
    hist = []
    continueCycle = True
    output = ['']
    while continueCycle:
        if cycle%40 == 0:
            output.append('')
        cycle += 1 # Aumentamos en 1 el ciclo
        currentLine, buffering, hist, toAdd, x, continueCycle = execute_cycle_logic(cycle, currentLine, buffering, hist, toAdd, x, input)
        if cycle== 9:
            d = 3
        output[-1] = output[-1] + check_if_draws(cycle, hist[-1])
    
    file = open('solutions/Day 10/output10_2.txt', 'w')
    for line in output:
        file.write(line)
        file.write('\n')
    file.close()
        

if __name__=='__main__':
    input = [line.removesuffix('\n') for line in open('solutions/Day 10/input10_1.txt', 'r').readlines()]
    problem1(input)
    problem2(input)