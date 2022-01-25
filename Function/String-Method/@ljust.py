file = open('./@ljust.py', 'a')


class vars:
    string = 'left'
    length = 20
    character = ' '


def printFile(string):
    print('# ', string, 'right', file=file, sep='')


vars.character = '@'
result = vars.string.ljust(vars.length, vars.character)
printFile(result)


# output:

# left@@@@@@@@@@@@@@@@right
