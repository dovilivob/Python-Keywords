file = open('./@splitlines.py', 'a')


class vars:
    string = 'FirstLine\n\tSecond\n\tThird'
    keeplinebreaks = False


def result():
    return vars.string.splitlines(vars.keeplinebreaks)


def printFile(string):
    print('# ' + str(string), file=file)


printFile(result())
vars.keeplinebreaks = True
printFile(result())

# out:

# ['FirstLine', '\tSecond', '\tThird']
# ['FirstLine\n', '\tSecond\n', '\tThird']
