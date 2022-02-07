file = open('./@@pop.py', 'a')


def printFile(string):
    print('# ' + str(string), file=file)


class vars:
    list = 'a b c d e f g h i'.split()
    position = 2


printFile('output: \n')
