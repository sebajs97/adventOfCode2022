# DAY 6: TUNING TROUBLE

# LINK: https://adventofcode.com/2022/day/6

def get_first_unique_char_qty(input: list, qty: int):
    currentLetters = []
    for i, l in enumerate(input):
        if l in currentLetters:
            cutPlace = currentLetters.index(l) + 1
            currentLetters = currentLetters[cutPlace:]
        currentLetters.append(l)
        if len(currentLetters) == qty:
            result = i+1
            break
    return result

def problem1(input):
    for item in input:
        result = get_first_unique_char_qty(item, 4)
        print(result)

def problem2(input):
    for item in input:
        result = get_first_unique_char_qty(item, 14)
        print(result)

if __name__=='__main__':
    input = [line.removesuffix('\n') for line in open('solutions/Day 6/input6_1.txt', 'r').readlines()]
    problem1(input)
    problem2(input)