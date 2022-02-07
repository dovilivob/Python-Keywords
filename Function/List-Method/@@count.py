file = open('./@@count.py', 'a')


def printFile(string):
    print('# ' + str(string), file=file)


class vars:
    list = 'a b c d e f g'.split()
    value = 'd'


printFile('output:\n')
printFile(vars.list.count(vars.value))
for i in range(29):
    vars.list.append(vars.value)
printFile(vars.list.count(vars.value))

# output:

# 1
# 30
