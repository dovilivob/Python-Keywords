file = open('./@reverse.py', 'a')


def printFile(string):
    print('# ' + str(string), file=file)


class vars:
    string = 'a b c d e f g h i'
    list = string.split(' ')


printFile('output: \n')
printFile(vars.list)
vars.list.reverse()
printFile(vars.list)
vars.string.reverse()
printFile(vars.string)
# output:

# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
# ['i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']
