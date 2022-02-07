file = open('@copy.py', 'a')


def printFile(string):
    print('# ' + str(string), file=file)


class vars:
    list = 'a b c d e f g'.split()


printFile('output:\n')
printFile(vars.list.copy())

# output:

# ['a', 'b', 'c', 'd', 'e', 'f', 'g']
