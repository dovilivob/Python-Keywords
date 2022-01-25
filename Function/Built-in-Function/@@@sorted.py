# Returns a sorted list of the specified iterable object


class vars: key, reverse = None, False


iterable, key, reverse = (1, 22, 43, 54, 222, 5, 2, 858), vars.key, vars.reverse

print(sorted(iterable, key=key, reverse=reverse))

# out:
#   [1, 2, 5, 22, 43, 54, 222, 858]
