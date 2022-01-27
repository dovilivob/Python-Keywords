# Adds zeros (0) at the beginning of the string, until it reaches the specified length.
# If the value of the len parameter is less than the length of the string, no filling is done.

file = open('./@zfill.py', 'a')


class vars:
    string = '42069'
    len = 10


def result():
    return vars.string.zfill(vars.len)


def printFile():
    print('# ' + result(), file=file)


printFile()
vars.string = '5387967816786'
printFile()
vars.string = '10.000'
printFile()

# out:

# 0000042069
# 5387967816786
# 000010.000
