# DAY 3: RUCKSACK REORGANIZATION

# LINK: https://adventofcode.com/2022/day/3

def get_unicode_val(character: str)-> int:
    if character.islower():
        return ord(character)-96
    # If the character is uppercase, then we have to add +26 to the return value
    return ord(character.lower())-96+26

def split_and_check_dup(line: str) -> int:
    half = int(len(line)/2)
    firstHalf = line[:half]
    secondHalf = line[half:]

    for letter in firstHalf:
        if letter in secondHalf:
            result = get_unicode_val(letter)
            return result
    return None

def find_badge(threeLinesList: list) -> str:
    Exception('No letter in common found')
    for letter in threeLinesList[0]:
        if (letter in threeLinesList[1]) and (letter in threeLinesList[2]):
            return letter

def problem_1(input):
    totalResult = 0
    for line in input:
        totalResult += split_and_check_dup(line)
    print(totalResult)

def problem_2(input):
    badgeSum = 0
    for i in range(int(len(input)/3)):
        startLine = i*3
        endLine = startLine + 3
        badgeLetter:str = find_badge(input[startLine : endLine])
        badgeSum += get_unicode_val(badgeLetter)
    print(badgeSum)

if __name__=='__main__':
    input = [line.removesuffix('\n') for line in open('solutions/Day 3/input3_1.txt', 'r').readlines()]
    problem_1(input)
    problem_2(input)