file = open('./@rsplit.py', 'a')


class vars:
    string = 'male, female, others'
    sep = ', '  # default: ' '
    maxsplit = -1  # all


def result():
    return vars.string.rsplit(vars.sep, vars.maxsplit)


def printFile(string):
    print('# ' + str(string), file=file)


printFile(result())
vars.maxsplit = 1
printFile(result())
vars.maxsplit = 0
printFile(result())

# out:

# ['male', 'female', 'others']
# ['male, female', 'others']
# ['male, female, others']
