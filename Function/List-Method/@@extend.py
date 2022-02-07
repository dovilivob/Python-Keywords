file = open('./@@extend.py', 'a')


def printFile(string):
    print('# ' + str(string), file=file)


class vars:
    a_extend = 'a b c d e f g'.split()
    a_append = a_extend.copy()
    b = list((1, 2, 3, 4, 5, 6, 7))


printFile('output:\n')

vars.a_append.append(vars.b)
vars.a_extend.extend(vars.b)

printFile(vars.a_append)
printFile(vars.a_extend)

# output:

# ['a', 'b', 'c', 'd', 'e', 'f', 'g', [1, 2, 3, 4, 5, 6, 7]]
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 1, 2, 3, 4, 5, 6, 7]
