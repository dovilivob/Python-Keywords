file = open('./@@join.py', 'a')


def printFile(string):
    print('#', string, file=file)


class values():
    iterable = {"name": "David", "id": 30, "country": "Taiwan"}
    separator = ' / '


iterable, separator = values.iterable, values.separator
printFile(separator.join(iterable))

iterable, separator = 'hello', ' ! '
printFile(separator.join(iterable))

# out:

# name / id / country
# h ! e ! l ! l ! o
