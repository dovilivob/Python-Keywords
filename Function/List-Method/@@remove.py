file = open('./@@remove.py', 'a')


def printFile(string):
    print('# ' + str(string), file=file)


class vars:
    list = 'a b c d e f g h i'.split()
    string = 'abcdefghi'
    element = 'c'


printFile('output: \n')
list, string, element = vars.list, vars.string, vars.element

printFile(list)
list.remove(element)
printFile(list)

printFile(string)
string.remove(element)
printFile(string)
# output:

# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
# ['a', 'b', 'd', 'e', 'f', 'g', 'h', 'i']
# abcdefghi
# AttributeError: 'str' object has no attribute 'remove'
