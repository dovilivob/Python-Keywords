file = open('./@@index.py', 'a')


def printFile(string):
    print('# ' + str(string), file=file)


class vars:
    list = 'a b c d e f g h i'.split()
    element = 'h'


printFile('output: \n')
printFile(vars.list.index(vars.element))
printFile(vars.list.find('j'))
printFile(vars.list.index('j'))
# output:

# 7
# AttributeError: 'list' object has no attribute 'find'
# ValueError: 'j' is not in list
