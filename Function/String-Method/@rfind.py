# Finds the last occurrence of the specified value.
# Returns -1 if the value is not found.
# Almost the same as the rindex()


file = open('./@rfind.py', 'a')


class vars:
    string = 'Hello how are you?'
    value = 'o'
    start = 0
    end = len(string)


def printFile(string):
    print('# ' + str(string), file=file)


def result():
    return vars.string.rfind(vars.value, vars.start, vars.end)


printFile(result())
vars.start, vars.end = 3, 8
printFile(result())

# out:

# 15
# 7
