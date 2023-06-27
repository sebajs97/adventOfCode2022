# DAY 11: MONKEY IN THE MIDDLE

# LINK: https://adventofcode.com/2022/day/11


from math import floor, prod
from collections import defaultdict

class Monkey():
    def __init__(self, items: list, op: list, divTest: int, monTrue: int, monFalse: int):
        self.items = items
        self.operation = op
        self.monTrue = monTrue
        self.monFalse = monFalse
        self.inspectCounter = 0
        self.divTest = divTest
        self.checked = {}

    def get_monkey_receiver(self, worryLevel):
        return self.monTrue if worryLevel % self.divTest == 0 else self.monFalse
    
    def get_monkey_receiver_factor(self, worryLevel: defaultdict):
        return self.monTrue if check_if_multiple(self.divTestFactor, worryLevel) else self.monFalse


def check_if_multiple(smallNumber: defaultdict, bigNumber: defaultdict)-> defaultdict:
    isMultiple = True
    for key, val in smallNumber.items():
        if key not in bigNumber.keys():
            isMultiple = False
            break
        else:
            if bigNumber[key] < val:
                isMultiple = False
                break
    return isMultiple

def update_worry_level(monOperation: list, worryLevel: int):
    operationTxt = monOperation[1]
    txt1 = monOperation[0]
    txt2 = monOperation[2]
    if txt1 == 'old':
        num1 = worryLevel
    else:
        num1 = int(txt1)
    if txt2 == 'old':
        num2 = worryLevel
    else:
        num2 = int(txt2)
    if operationTxt == '*':
        return num1 * num2
    else:
        return num1 + num2


#### FUNCIONES AUXILIARES

def create_monkeys(input: list)-> dict:
    monkeys = {}
    for line in input:
        instr = line.strip()
        if instr.startswith('Monkey'):
            n = instr.replace('Monkey ', '')
            n = n.replace(':', '')
            currentMonkey = int(n)
            continue
        if instr.startswith('Starting items: '):
            items = instr.replace('Starting items: ', '')
            items = items.replace(' ', '')
            items = items.split(',')
            items = [int(i) for i in items]
        elif instr.startswith('Operation:'):
            operation = instr.replace('Operation: new = ', '')
            operation = operation.split(' ')
        elif instr.startswith('Test'):
            test = instr.replace('Test: divisible by ', '')
            test = int(test)
        elif instr=='':
            pass
        else:
            if instr.startswith('If true:'):
                monTrue = instr.replace('If true: throw to monkey ', '')
                monTrue = int(monTrue)
            else:
                monFalse = instr.replace('If false: throw to monkey ', '')
                monFalse = int(monFalse)
                monkeys[currentMonkey] = Monkey(items, operation, test, monTrue, monFalse)
    return monkeys
 
def let_monkeys_play(monkeys: dict) -> dict:
    for key, monkey in monkeys.items():
        for i in range(len(monkey.items)):
            currentWorryLevel = monkeys[key].items[i]
            currentWorryLevel = update_worry_level(monkey.operation, currentWorryLevel)
            currentWorryLevel = floor(currentWorryLevel / 3)
            mReceiver = monkey.get_monkey_receiver(currentWorryLevel)
            monkeys[mReceiver].items.append(currentWorryLevel)
            monkeys[key].inspectCounter += 1
        monkeys[key].items = []
    return monkeys

def let_monkeys_play2(monkeys: dict) -> dict:
    superMod = prod([m.divTest for m in monkeys.values()])
    for key, monkey in monkeys.items():
        for i in range(len(monkey.items)):
            currentWorryLevel = monkeys[key].items[i]
            currentWorryLevel = update_worry_level(monkey.operation, currentWorryLevel)
            currentWorryLevel = currentWorryLevel % superMod
            mReceiver = monkey.get_monkey_receiver(currentWorryLevel)
            monkeys[mReceiver].items.append(currentWorryLevel)
            monkeys[key].inspectCounter += 1
        monkeys[key].items = []
    return monkeys

def get_result(monkeys: dict):
    topValues = [m.inspectCounter for m in monkeys.values()]
    topValues.sort()
    result = topValues[-1] * topValues[-2]
    return result

#### RESOLUCIÓN DE PROBLEMAS

def problem1(input: list):
    monkeys = create_monkeys(input)
    for round in range(20):
        monkeys = let_monkeys_play(monkeys)
    result = get_result(monkeys)
    print(result)

def problem2(input: list):
    monkeys = create_monkeys(input)
    for round in range(10000):
        monkeys = let_monkeys_play2(monkeys)
    result = get_result(monkeys)
    print(result)

if __name__=='__main__':
    input = [line.removesuffix('\n') for line in open('solutions/Day 11/input11_1.txt', 'r').readlines()]
    problem1(input)
    problem2(input)