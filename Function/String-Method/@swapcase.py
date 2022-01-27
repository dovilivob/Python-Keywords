# Make the lower case letters upper case
# and the upper case letters lower case.

file = open('./@swapcase.py', 'a')


class vars:
    string = 'OkOKoK'


def result():
    return vars.string.swapcase()


def printFile():
    print('# ' + vars.string, str(result()),
          sep='\t'.expandtabs(10-len(vars.string)), file=file)


arr = list(('upper', 'LOWER', 'Mixed', 'dAVID'))

for element in arr:
    vars.string = element
    printFile()


# upper ----> UPPER
# LOWER ----> lower
# Mixed ----> mIXED
# dAVID ----> David
