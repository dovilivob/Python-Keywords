# return to specify how to slice a sequence.
# You can specify where to start the slicing,
# and where to end. You can also specify the step,
# which allows you to e.g. slice only every other item.

start = 0
end = 2
step = 1
x = slice(start, end, step)

a = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i')
x = slice(0, 6, 2)
print(a[x])
# Output:
#   ('a', 'c', 'e')
