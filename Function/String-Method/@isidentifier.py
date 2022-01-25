# A string is considered a valid identifier if it only contains
# alphanumeric letters (a - z, 0 - 9), or underscores ( _ )
# And also can't start with a number, or contain any space


def stuff(arr):
    for element in arr:
        print(element, element.isidentifier(), sep=': ')


stuff(['Demo', 'myFolder', 'demo004', '2bring', 'my file'])

# out:

# Demo: True
# myFolder: True
# demo004: True
# 2bring: False
# my file: False
