file = open('./@@@replace.py', 'a')

class vars:
    old = 'old'
    new = 'new'
    count = 3
    
def printFile(string):
    print('# ' + str(string), file=file)
    
string = 'old old old old old old! bla bla bla bla...'

result = string.replace(vars.old, vars.new)
printFile(result)

result = string.replace(vars.old, vars.new, vars.count)
printFile(result)

# out:

# new new new new new new! bla bla bla bla...
# new new new old old old! bla bla bla bla...
