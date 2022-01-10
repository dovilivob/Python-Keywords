# Returns an unchangeable frozenset object


myList = ['a', 'b', 'c']
x = frozenset(myList)

x[1] = 'B'
# Output:
#   TypeError: 'frozenset' object does not support item assignment
