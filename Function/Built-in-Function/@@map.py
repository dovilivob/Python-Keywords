# map(function, iterable)
# Executes a specified function for each item in an iterable.
# the item is sent to the function as a parameter


def myfunc(n):
    return len(n)


x = map(myfunc, ('apple', 'banana', 'Canada'))
print(list(x))
# Output: [5, 6, 6]

def plus(a, b):
    return a + b

x = map(plus, (1, 3, 4), (3, 5, 7))
print(list(x))
# Output: [4, 8, 11]
