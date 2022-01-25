# Finds the first occurrence of the specified value.
# Returns -1 if the value is not found.
# The find() is almost the same as the index() method, the only difference is that the index() raises an exception if the value is not found.

string = 'Hi There, are you Okay?'
(value, start, end) = ('e', 0, len(string))

n = string.find(value, start, end)
print(n)
# out: 5

start = n + 1
print(string.find(value, start, end))
# out: 7

value = '@'
print(string.find(value))
# out: -1

print(string.index(value))
# out: 
#   ValueError: substring not found
