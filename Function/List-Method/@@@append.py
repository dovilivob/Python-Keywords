file = open('./@@@append.py', 'a')

def printFile(string):
    print('# ' + str(string), file=file)

class vars:
    list = []
    element = 'element'
    
vars.list.append(vars.element)

printFile(vars.list)
vars.element  = list(('this', 'is', 'a', 'list'))
vars.list.append(vars.element)
printFile(vars.list)
# output:

# ['element']
# ['element', ['this', 'is', 'a', 'list']]
