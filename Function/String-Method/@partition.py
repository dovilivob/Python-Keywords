# Searches for a specified string, 
# and splits the string into a tuple containing three elements (x, y, z).

# x - the part before the specified string
# y - the specified string
# z - the part after the string

file = open('./@partition.py', 'a')

class vars:
    string = 'This is a string'
    value = 'is '
    
def printFile(string):
    print('# ' + str(string), file=file)
    
result = vars.string.partition(vars.value)
printFile(result)
printFile(result[2])

# out:

# ('Th', 'is ', 'is a string')
# is a string
