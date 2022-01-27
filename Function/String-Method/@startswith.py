file = open('./@startswith.py', 'a')


class vars:
    string = "Hello everyone this is me!"
    value = 'eve'
    start = 6
    end = len(string)


def result():
    return vars.string.startswith(vars.value, vars.start, vars.end)


def printFile():
    print('# ' + str(result()), file=file)


printFile()
vars.start = 0
printFile()

# out:

# True
# False
