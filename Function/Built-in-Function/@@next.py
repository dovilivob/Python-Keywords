# next(iterable, default)

# default: Optional,
# An default value to return if the iterable has reached its end.

arr = iter(['elephant', 'zebra', 'lion', 'butterfly'])

print(next(arr))
# output: elephant
print(next(arr))
# output: zebra
print(next(arr))
# output: lion
print(next(arr))
# output: butterfly
print(next(arr, 'end'))
# output: end
print(next(arr, 'end you fuck'))
# output: end you fuck
