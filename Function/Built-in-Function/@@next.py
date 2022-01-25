# next(iterable, default)

# default: Optional,
# An default value to return if the iterable has reached its end.

arr = iter(['elephant', 'zebra', 'lion', 'butterfly'])

print(next(arr))
# out: elephant
print(next(arr))
# out: zebra
print(next(arr))
# out: lion
print(next(arr))
# out: butterfly
print(next(arr, 'end'))
# out: end
print(next(arr, 'end you fuck'))
# out: end you fuck
