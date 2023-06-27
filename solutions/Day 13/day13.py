# DAY 13: DISRTESS SIGNAL

# LINK: https://adventofcode.com/2022/day/13

from copy import copy
from math import floor

### FUNCIONES AUXILIARES
def format_data(input: list):
    data = []
    for line in input:
        if line != '':
            data.append(read_line(line)[0])
    return data

def read_line(line: list, currentPos = 0, lista = None):
    symbols1 = [',', ']', '[']
    while currentPos < len(line):
        if lista == None:
            lista = []
            currentPos += 1
        elif line[currentPos] == '[':
            branch = read_line(line, currentPos)
            lista.append(branch[0][:])
            currentPos = branch[1] + 1
        elif line[currentPos] == ']':
            return lista, currentPos
        elif line[currentPos] == ',':
            currentPos += 1
        else:
            numLen = 0
            while line[currentPos + numLen] not in symbols1:
                numLen += 1
            lista.append(int(line[currentPos:currentPos+numLen]))
            currentPos += numLen


def compare_two_lists(l1, l2):
    index = 0
    compareResult = None
    while (index<len(l1) and compareResult==None):
        if index >= len(l2):
            compareResult = False
            break
        l1sub = copy(l1[index])
        l2sub = copy(l2[index])
        if (type(l1sub) == int) and (type(l2sub) == int):
            if l1sub<l2sub:
                compareResult = True
                break
            elif l1sub>l2sub:
                compareResult = False
                break
        else:
            l1sub = l1sub if (type(l1sub) == list) else [l1sub]
            l2sub = l2sub if (type(l2sub) == list) else [l2sub]
            compareResult = compare_two_lists(l1sub, l2sub)
        index += 1
    if len(l1)==0 and len(l2)>0 and compareResult==None:
        compareResult = True
    if len(l1)==index and len(l2)>len(l1) and compareResult==None:
        compareResult = True
    return compareResult

def sum_of_true_indices(pairsComparison: list):
    trueList = [i+1 for i, p in enumerate(pairsComparison) if p]
    return sum(trueList)

def a_lower_than_b(packetA, packetB):
    return compare_two_lists(packetA, packetB)

def binary_store_position(currentList: list, packet: list):
    if currentList==[]:
        return 0
    else:
        half = floor(len(currentList)/2)
        aIsLower = a_lower_than_b(currentList[half], packet)
        if aIsLower:
            return 1 + half + binary_store_position(currentList[half+1:], packet)
        else:
            return binary_store_position(currentList[:half], packet)


### RESOLUCION DE PROBLEMAS
def problem1(input: list):
    data = format_data(input)
    pairsComparison = []
    for i in range(int(len(data)/2)):
        index1 = i*2
        index2 = i*2+1
        pairsComparison.append(compare_two_lists(data[index1], data[index2]))
    
    pairsComparison = [p if p!=None else True for p in pairsComparison]
    
    result = sum_of_true_indices(pairsComparison)
    print(result)

def problem2(input: list):
    data = format_data(input)
    sortedList = []
    dividerPackets = [[[2]], [[6]]]
    for packet in data:
        pos = binary_store_position(sortedList, packet)
        sortedList.insert(pos, packet[:])
    pos1 = binary_store_position(sortedList, dividerPackets[0])
    sortedList.insert(pos, dividerPackets[0][:])
    pos2 = binary_store_position(sortedList, dividerPackets[1])
    sortedList.insert(pos, dividerPackets[1][:])
    result = (pos1+1) * (pos2+1)
    print(result)


if __name__=='__main__':
    input = [line.removesuffix('\n') for line in open('solutions/Day 13/input13_1.txt', 'r').readlines()]
    problem1(input)
    problem2(input)