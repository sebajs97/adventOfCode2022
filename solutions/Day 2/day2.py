# DAY 2: ROCK, PAPER AND SCISSORS

# LINK: https://adventofcode.com/2022/day/2

def check_game_1(opt1: str, opt2: str) -> int:
    equivalencies = {'X': 'A', 'Y': 'B', 'Z': 'C'}
    values = {'A': 1, 'B': 2, 'C':3}
    loosingMatches = [['A', 'C'], ['B', 'A'], ['C', 'B']]

    selection1 = opt1
    if opt2 in equivalencies.keys():
        selection2 = equivalencies[opt2]
    else:
        selection2 = opt2
    
    selectionPoints = values[selection2]
    if selection1 == selection2:
        # Draw
        resultPoints = 3
    elif [selection1, selection2] in loosingMatches:
        resultPoints = 0
    else:
        resultPoints = 6

    finalPoints = selectionPoints + resultPoints
    return finalPoints

def check_game_2(opt1: str, opt2: str) -> int:
    valuesSelection = {'A': 1, 'B': 2, 'C':3}
    valuesResult = {'X': 0, 'Y': 3, 'Z': 6}
    winningMatches = {'A': 'C', 'B': 'A', 'C': 'B'}
    loosingMatches = {'A': 'B', 'B': 'C', 'C': 'A'}
    
    if opt2 == 'X':
        selection2 = winningMatches[opt1]
    elif opt2 == 'Y':
        selection2 = opt1
    else:
        selection2 = loosingMatches[opt1]
    selectionPoints = valuesSelection[selection2]
    resultPoints = valuesResult[opt2]
    return selectionPoints + resultPoints

def problem_1(input):
    input = [l.split(' ') for l in input]

    resultSum = 0
    for game in input:
        resultSum += check_game_1(game[0], game[1])
    print(resultSum)

def problem_2(input):
    input = [l.split(' ') for l in input]

    resultSum = 0
    for game in input:
        resultSum += check_game_2(game[0], game[1])
    print(resultSum)

if __name__=='__main__':
    input = [line.removesuffix('\n') for line in open('solutions/Day 2/input2_1.txt', 'r').readlines()]
    problem_1(input)
    problem_2(input)