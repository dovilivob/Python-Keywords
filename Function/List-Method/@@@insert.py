file = open('./@@@insert.py', 'a')


def printFile(string):
    print('# ' + str(string), file=file)


class vars:
    list = 'a b d e f g h i'.split()
    element = 'c'


printFile('output: \n')

printFile(vars.list)
vars.list.insert(2, vars.element)
printFile(vars.list)

# output:

# ['a', 'b', 'd', 'e', 'f', 'g', 'h', 'i']
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
