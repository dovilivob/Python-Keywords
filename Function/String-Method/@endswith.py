# Returns True if the string ends with the specified value, otherwise False

string = "Hello, welcome to my world!"

(value, start, end) = ('.', 0, len(string))

print(string.endswith(value, start, end))
# out: False

value = 'my world!'
print(string.endswith(value, start, end))
# out: True