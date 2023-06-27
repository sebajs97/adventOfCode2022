## DAY 1: CALORIE COUNTING

## Link: https://adventofcode.com/2022/day/1

def problem_1(input):
    currentCalories = 0
    maxCalories = 0

    for line in input:
        if line == '':
            maxCalories = max(currentCalories, maxCalories)
            currentCalories = 0
        else:
            calories = int(line)
            currentCalories += calories

    maxCalories = max(currentCalories, maxCalories)
    print(maxCalories)

def problem_2(input):
    currentCalories = 0
    maxCalories = [0, 0, 0]

    for line in input:
        if line == '':
            maxCalories[-1] = max(currentCalories, maxCalories[-1])
            maxCalories.sort(reverse=True)
            currentCalories = 0
        else:
            calories = int(line)
            currentCalories += calories

    maxCalories[-1] = max(currentCalories, maxCalories[-1])
    print(sum(maxCalories))

if __name__=="__main__":
    input = [line.removesuffix('\n') for line in open('solutions/Day 1/input1_1.txt', 'r').readlines()]
    problem_1(input)
    problem_2(input)