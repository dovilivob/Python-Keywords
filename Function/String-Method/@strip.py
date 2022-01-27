file = open('./@strip.py', 'a')


class vars:
    string = 'OkOKoK'
    char = '@'


def result():
    return vars.string.strip(vars.char)


def printFile():
    print('# ' + str(result()), file=file)


printFile()
vars.char = 'O'
printFile()
vars.string, vars.char = "ddd...ssiej***", 'd.si'
printFile()
vars.char = "*."
printFile()

# out:

# OkOKoK
# kOKoK
# ej***
# ddd...ssiej
