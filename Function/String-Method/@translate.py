# Returns a string where some specified characters are replaced with the character described in a dictionary or in a mapping table.
# Use the maketrans() to create a mapping table.
# If a character is not specified in the dictionary/ table, the character will not be replaced.
# If you use a dictionary, you must use ascii codes instead of characters.

file = open('./@translate.py', 'a')


class vars:
    string = "Hello guys I'm Wayne, and also I'm a gay person."
    x, y = 'Wayne', 'Jerry'
    z = ''
    table = string.maketrans(x, y)


def result():
    vars.table = vars.string.maketrans(vars.x, vars.y)
    return vars.string.translate(vars.table)


def printFile():
    print('# ' + str(vars.table), file=file)
    print('# ' + result(), file=file)


printFile()
vars.string = 'Wayne is homo'
printFile()

# out:
# {87: 74, 97: 101, 121: 114, 110: 114, 101: 121}
# Hyllo gurs I'm Jerry, erd elso I'm e ger pyrsor.
# {87: 74, 97: 101, 121: 114, 110: 114, 101: 121}
# Jerry is homo
