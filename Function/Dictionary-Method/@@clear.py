import os
pwd = os.path.abspath(__file__)

file = open(pwd, 'a')


def printFile(string):
    print('# ' + str(string) + '\n', file=file)


printFile('')
printFile('output:')


class vars:
    dict = {
        "name": "David",
        "gender": "male",
        "age": 20
    }


vars.dict.clear()
printFile(vars.dict)

# output:

# {}
