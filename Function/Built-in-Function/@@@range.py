# Returns a sequence of numbers,
# starting from 0 by default,
# and increments by 1 by default,
# and stops before a specified number.

# range(start, stop, step)
# step: An integer specifying the incrementation.
# Default 1

x = range(3)

for n in x:
    print(n)
# Output:
# 0
# 1
# 3

for i in range(8, 90, 12):
    print(i)
# Output:
# 8
# 20
# 32
# 44
# 56
# 68
# 80
