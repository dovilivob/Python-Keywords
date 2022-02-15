import os
pwd = os.path.abspath(__file__)

file = open(pwd, 'a')


def printFile(string):
    print('# ' + str(string) + '\n', file=file)


class vars:
    iterable = ['Ford', 'shit', 'BMW', 'Volvo',
                '9581', 'lowercaseletters']
    reverse = True

    def myFunc(e):
        return int(e.isupper())
    key = myFunc


print()
printFile('output: ')
vars.iterable.sort(reverse=vars.reverse)
printFile(vars.iterable)
vars.iterable.sort(reverse=vars.reverse, key=vars.key)
printFile(vars.iterable)

# output:
# ['shit', 'lowercaseletters', 'Volvo', 'Ford', 'BMW', '9581']
# ['BMW', 'shit', 'lowercaseletters', 'Volvo', 'Ford', '9581']


def myFunc(e):
    return e['rate']


vars.iterable = [
    {'movie': 'Pulp Fiction', 'rate': 10},
    {'movie': 'The Hateful Eight', 'rate': 7},
    {'movie': 'Once apon a time in ...Hollywood', 'rate': 9}
]

vars.iterable.sort(reverse=vars.reverse, key=myFunc)

printFile(vars.iterable)

# output:

# [{'movie': 'Pulp Fiction', 'rate': 10}, {'movie': 'Once apon a time in ...Hollywood', 'rate': 9}, {'movie': 'The Hateful Eight', 'rate': 7}]
