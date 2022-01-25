# Returns a mapping table that can be used with the translate()
# to replace specifired characters.

file = open('./@maketrans.py', 'a')


class vars:
    string = 'Hello David'
    origin = 'iadDv'
    new = 'rhete'
    delete = 'ole'


def printFile(string):
    print('# ' + string, file=file)


table = vars.string.maketrans(vars.origin, vars.new)
printFile(str(table))
printFile(vars.string.translate(table))
printFile('\n')

table = vars.string.maketrans(vars.origin, vars.new, vars.delete)
printFile(str(table))
printFile(vars.string.translate(table))
printFile('\n')

# output:

# {105: 114, 97: 104, 100: 101, 68: 116, 118: 101}
# Hello there
# 

# {105: 114, 97: 104, 100: 101, 68: 116, 118: 101, 111: None, 108: None, 101: None}
# H there
# 

