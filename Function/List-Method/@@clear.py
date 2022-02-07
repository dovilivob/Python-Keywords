file = open('./@@clear.py', 'a')


def printFile(string):
    print('# ' + str(string), file=file)


class vars:
    list = 'a b c d e f g'.split()


printFile('output:\n')

printFile(vars.list)
vars.list.clear()
printFile(vars.list)

# output:

# ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# []
