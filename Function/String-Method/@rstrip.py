file = open('./@rstrip.py', 'a')


class vars:
    string = '   hello   '
    char = ' '  # default ' '


def result():
    return vars.string.rstrip(vars.char)


def printFile(string):
    print('# ' + str(string), file=file)


out = "I don't know what is " + result() + 'kitty'
printFile(out)
vars.string, vars.char = 'banana,,,,,ssqqqww.....', ",.qsw"
printFile(result())

# out:

# I don't know what is    hellokitty
# banana
