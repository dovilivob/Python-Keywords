# Deleting the leading characters, Default ' '

file = open('./@lstrip.py', 'a')

class vars:
    char = ' '
    string = '  fuck    '
    

def printFile(string):
    print('# ' + string, file=file)


result = vars.string.lstrip()
result = ' '.join(['what the', result, 'is going on?'])
printFile(result)

result = vars.string.lstrip(vars.char)
result = ' '.join(['what the', result, 'is going on?'])
printFile(result)

vars.string, vars.char = 'aaabbssddcc##...#@#lalaladododo', 'absdc#.#@#'
result = vars.string.lstrip(vars.char)
printFile(result)

# output:

# what the fuck     is going on?
# what the fuck     is going on?
# lalaladododo
