# DAY 5: SUPPLY STACKS

# LINK: https://adventofcode.com/2022/day/5

import re

def decompose_line(line, stacks):
    i = 0
    while (i*4 < len(line)):
        start = i*4
        end = i*4+4
        chars = line[start:end]
        if chars.strip()!='':
            stacks[i].insert(0, str(chars[1]))
        i+=1
    return stacks

def fix_input(input):
    rePattern = r'move (\d+) from (\d+) to (\d+)'
    movements = []
    # TODO Check the amount of stacks
    numberOfStacks = int((len(input[0]) + 1)/4)
    stacks = [[] for i in range(numberOfStacks)]

    for line in input:
        if line.startswith('move'):
            vals = re.search(rePattern, line).groups()
            movements.append([int(n) for n in vals])
        elif line == '':
            pass
        elif line.startswith(' 1 '):
            pass
        else:
            stacks = decompose_line(line, stacks)
    return stacks, movements

def next_move_1(stacks: list, move: list):
    qtyToMove, frm, to = move[:]
    frm -= 1
    to -= 1
    for i in range(qtyToMove):
        stacks[to].append(stacks[frm].pop())
    return stacks

def next_move_2(stacks: list, move: list):
    qtyToMove, frm, to = move[:]
    frm -= 1
    to -= 1
    movingStacks = stacks[frm][-qtyToMove:]
    stacks[frm] = stacks[frm][:-qtyToMove]
    stacks[to] = stacks[to] + movingStacks[:]
    return stacks


def problem1(input):
    stacks, movements = fix_input(input)
    for m in movements:
        stacks = next_move_1(stacks, m)
    result = [l.pop() for l in stacks]
    result = ''.join(result)
    print(result)


def problem2(input):
    stacks, movements = fix_input(input)
    for m in movements:
        stacks = next_move_2(stacks, m)
    result = [l.pop() for l in stacks]
    result = ''.join(result)
    print(result)


if __name__=='__main__':
    input = [line.removesuffix('\n') for line in open('solutions/Day 5/input5_1.txt', 'r').readlines()]
    problem1(input)
    problem2(input)