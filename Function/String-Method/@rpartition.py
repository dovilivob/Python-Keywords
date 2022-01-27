file = open('./@rpartition.py', 'a')


class vars:
    string = "I love doing things, I mean really, me do things a lot!"
    value = 'things'


def result():
    return vars.string.rpartition(vars.value)


def printFile(string):
    print('# ' + str(string), file=file)


printFile(result())
printFile(result()[1])

# out:

# ('I love doing things, I mean really, me do ', 'things', ' a lot!')
# things
