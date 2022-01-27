

file = open('./@rjust.py', 'a')


class vars:
    string = 'blablaBLA'
    length = 20
    char = ' '


def printFile(string):
    print('# ' + str(string), file=file)


def result():
    return vars.string.rjust(vars.length, vars.char)


printFile(result())
vars.length, vars.char = 44, '!'
printFile(result())
vars.string, vars.length = 'g', 10
printFile(result())

# out:

#            blablaBLA
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!blablaBLA
# !!!!!!!!!g
