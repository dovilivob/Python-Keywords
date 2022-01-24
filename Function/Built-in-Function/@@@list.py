# Creates a list object
# list(iterable)


Dict = ('a', 'b', 'c')
result = list(Dict)
print(result)
# Output:
#   ['a', 'b', 'c']

Dict = dict(a=3, b=2, c=1)
result = list(Dict)
print(result)
# Output:
#   ['a', 'b', 'c']

string = 'apple'
result = list(string)
# Output:
#   ['a', 'p', 'p', 'l', 'e']