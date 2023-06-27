# DAY 4: CAMP CLEANUP

# LINK: https://adventofcode.com/2022/day/4

def clean_input(input: list) -> list:
    cleanedInput = []
    for line in input:
        assingmentPair = line.split(',')
        assingmentPair = [[int(i) for i in rang.split('-')] for rang in assingmentPair]
        cleanedInput.append(assingmentPair)
    return cleanedInput

def check_if_fully_overlaps(pairRange: list) -> bool:
    if (pairRange[0][0] <= pairRange[1][0]) and (pairRange[0][1] >= pairRange[1][1]):
        return True
    elif (pairRange[0][0] >= pairRange[1][0]) and (pairRange[0][1] <= pairRange[1][1]):
        return True
    return False

def num_in_interval(interval: list, num: int):
    if (num>=interval[0] and num<=interval[1]):
        return True
    return False

def check_quantity_overlaped(pairRange: list) -> int:
    #  NOTE No era necesario hacer esta función así.
    # bastaba solo con verificar si estaban superpuestos o no,
    # no era necesario ver la cantidad superpuesta.
    for i in range(2):
        pairA = pairRange[i]
        pairB = pairRange[i-1]
        if num_in_interval(pairA, pairB[0]):
            minVal = min(pairA[1], pairB[1])
            return abs(pairB[0]-minVal)+1
        elif (num_in_interval(pairA, pairB[1])):
            maxVal = max(pairA[0], pairB[0])
            return abs(pairB[1]-maxVal)+1
    return None

def problem_1(input: list):
    pairCombinations = clean_input(input)
    fullyContained = [check_if_fully_overlaps(comb) for comb in pairCombinations]
    countFullyContained = fullyContained.count(True)
    print(countFullyContained)

def problem_2(input: list):
    pairCombinations = clean_input(input)
    quantityOverlaped = [check_quantity_overlaped(comb) for comb in pairCombinations]
    print(sum([1 for a in quantityOverlaped if a!=None]))

if __name__=='__main__':
    input = [line.removesuffix('\n') for line in open('solutions/Day 4/input4_1.txt', 'r').readlines()]
    problem_1(input)
    problem_2(input)