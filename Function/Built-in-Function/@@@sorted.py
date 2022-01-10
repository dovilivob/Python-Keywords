# Returns a sorted list of the specified iterable object

iterable = (1, 22, 43, 54, 222, 5, 2, 858)
key = None
reverse = False

print(sorted(iterable, key=key, reverse=reverse))
# Output:
#   [1, 2, 5, 22, 43, 54, 222, 858]
