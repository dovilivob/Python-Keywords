# next(iterable, default)

# default: Optional,
# An default value to return if the iterable has reached its end.

arr = iter(['elephant', 'zebra', 'lion', 'butterfly'])

print(next(arr))
# Output: elephant
print(next(arr))
# Output: zebra
print(next(arr))
# Output: lion
print(next(arr))
# Output: butterfly
print(next(arr, 'end'))
# Output: end
print(next(arr, 'end you fuck'))
# Output: end you fuck
