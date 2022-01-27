file = open('./@title.py', 'a')


class vars:
    string = 'OkOKoK'


def result():
    return vars.string.title()


def printFile():
    print('# ' + vars.string, str(result()),
          sep='\t'.expandtabs(10-len(vars.string)), file=file)


arr = list(('upper', 'Mixed', 'dAVID', '__!!ah', '69king'))

for element in arr:
    vars.string = element
    printFile()


# upper ----> Upper
# dAVID ----> David
# Mixed ----> Mixed
# __!!ah ---> __!!Ah
# 69king ---> 69King
