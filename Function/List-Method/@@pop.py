file = open('./@@pop.py', 'a')


def printFile(string):
    print('# ' + str(string), file=file)


class vars:
    list = 'a b c d e f g h i'.split()
    position = 2


printFile('output: \n')
list, position = vars.list, vars.position

printFile(list)
printFile(list.pop(position))
printFile(list)
# output:

# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
# c
# ['a', 'b', 'd', 'e', 'f', 'g', 'h', 'i']
