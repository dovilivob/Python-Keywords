# Returns the number of times a specified value appears in the string

string = "I love mango, it's my favorite fruit"

(value, start, end) = ('apple', 0, len(string))


print(string.count(value, start, end))
# Output: 0

value = 'mango'
print(string.count(value, start, end))
# Output: 1

value = 'i'
print(string.count(value, start, end))
# Output: 3
