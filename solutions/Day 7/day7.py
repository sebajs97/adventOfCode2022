# DAY 7: NO SPACE LEFT ON DEVICE

# LINK: https://adventofcode.com/2022/day/7

def read_cd_instruction(routeStack, instruction):
    secondCommand = instruction[3:]
    if secondCommand == '':
        asdf=3
    if secondCommand == '..':
        # Volvemos atrás, por lo que el stack recibe un pop
        routeStack.pop()
    elif secondCommand == '/':
        routeStack = ['/']
    else:
        #  Se está accediendo a un folder, por lo que hacemos
        # un append al Stack.
        routeStack.append(secondCommand)

def set_child(newChild, routeStack :list, tree:dict):
    nav = tree
    for r in routeStack[:-1]:
        nav = nav[r]['childs']
    nav[routeStack[-1]] = newChild
        
def read_line(routeStack, line, tree):
    if line.startswith('$ '):
        instruction = line[2:]
        if instruction.startswith('cd'):
            read_cd_instruction(routeStack, instruction)
    else:
        if line.startswith('dir'):
            name = line[4:]
            newChild = {'childs':{}}
        else:
            size, name = line.split(' ')
            size = int(size)
            newChild = {'size':size}
        if name=='':
            pass
        routeStack.append(name)
        set_child(newChild, routeStack, tree)
        routeStack.pop()
    return routeStack, tree

def get_folder_sizes(routeStack, parentProperties, cumulative: dict):
    folderSize = 0
    for name in parentProperties['childs']:
        properties = parentProperties['childs'][name]
        if 'childs' in properties.keys():
            routeStack.append(name)
            size, cumulative = get_folder_sizes(routeStack, properties, cumulative)
            routeStack.pop()
            folderSize += size
        elif 'size' in properties.keys():
            folderSize += properties['size']

    saveName = '/'.join(routeStack)
    if saveName in cumulative:
        cumulative[saveName] += folderSize
    else:
        cumulative[saveName] = folderSize
    return folderSize, cumulative

def visual_output_tree(file, tree: dict, indent:int =0):
    indentTxt = '\t'*indent
    for name, properties in tree.items():
        if 'size' in properties.keys():
            size = properties['size']
            outputName = f'{name}, {size}'
        else:
            outputName = f'{name} - (dir)'
        file.write(f'{indentTxt}{outputName}\n')
        if 'childs' in properties.keys():
            visual_output_tree(file, tree[name]['childs'], indent+1)

def get_all_folder_sizes(input: list):
    routeStack = ['/']

    # Creamos el arbol 
    tree = {'/':{'childs':{}}}
    # Llenamos el arbol con los childs y sus propiedades
    for line in input:
        routeStack, tree = read_line(routeStack, line, tree)

    # Ahora vamos a revisar calcular el tamaño de cada folder
    folderSize, cumulative = get_folder_sizes(['/'], tree['/'], {})
    return folderSize, cumulative

def problem1(input):
    folderSize, cumulative = get_all_folder_sizes(input)

    # Finalmente, solo contamos los folders que tengan un tamaño menor a 1000000
    result = 0
    for value in cumulative.values():
        if value <= 100000:
            result += value
    print(result)


def problem2(input):
    totalSpace = 70000000
    requiredSpace = 30000000
    folderSize, cumulative = get_all_folder_sizes(input)
    minRequiredSpace = folderSize - (totalSpace - requiredSpace)
    biggerThanRequiredSpace = [val for val in cumulative.values() if val>=minRequiredSpace]
    result = min(biggerThanRequiredSpace)
    print(result)


if __name__ == '__main__':
    input = [line.removesuffix('\n') for line in open('solutions/Day 7/input7_1.txt', 'r').readlines()]
    problem1(input)
    problem2(input)