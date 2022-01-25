# Returns an iterator were the items are filtered through a function to test if the item is accepted or not.

# filter(function, iterable)

ages = [4, 23, 22, 55, 10, 32, 5, 92]

def func(x):
    if x < 18:
        return 0
    else:
        return 1

adults = filter(func, ages)

for x in adults:
    print(x)
    
# out: 
# 23
# 22
# 55
# 32
# 92
