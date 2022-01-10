# Creates a list object
# list(iterable)

x = list(('a', 'b', 'c'))
print(x)
# Output:
#   ['a', 'b', 'c']

x = list(dict(a=3, b=2, c=1))
print(x)
# Output:
#   ['a', 'b', 'c']

x = list('apple')
# Output:
#   ['a', 'p', 'p', 'l', 'e']