# Finds the first occurrence of the specified value.
# Returns -1 if the value is not found.
# The find() is almost the same as the index() method, the only difference is that the index() raises an exception if the value is not found.

string = 'Hi There, are you Okay?'
(value, start, end) = ('e', 0, len(string))

n = string.find(value, start, end)
print(n)
# Output: 5

start = n + 1
print(string.find(value, start, end))
# Output: 7

value = '@'
print(string.find(value))
# Output: -1

print(string.index(value))
# Output: 
#   ValueError: substring not found
