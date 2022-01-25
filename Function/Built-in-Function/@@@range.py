# Returns a sequence of numbers,
# starting from 0 by default,
# and increments by 1 by default,
# and stops before a specified number.

# range(start, stop, step)
# step: An integer specifying the incrementation.
# Default 1

class vars: start, step = 0, 1

x = range(3)

for n in x:
    print(n)
    
# out:
# 0
# 1
# 3

start, end, step = 8, 90, 12

for i in range(start, end, step):
    print(i)
    
# out:
# 8
# 20
# 32
# 44
# 56
# 68
# 80
