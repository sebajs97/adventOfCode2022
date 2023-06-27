def basic_read(fileName) -> list:
    file = open(fileName, 'r')
    inputText = [line.removesuffix('\n') for line in file.readlines()]
    return inputText

