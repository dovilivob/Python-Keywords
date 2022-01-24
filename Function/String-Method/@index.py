# The index() is almost the same as the find()
# The only difference is that the find() returns -1 if the value is not found.

string = 'Hello, are you alright?'


class vars: (value, start, end) = ('a', 0, len(string))


(value, start, end) = (vars.value, vars.start, vars.end)

result = string.index(value, start, end)

print(result)
# Output: 7

print(string.find('q'))
# Output: -1

print(string.index('q'))
# Output:
#   ValueError: substring not found
