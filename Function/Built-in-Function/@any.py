# Basically the opposite of all()

# any(iterable X)
# if anything in X is not False (0, empty, None, False):
#   return True
# else:
#   return False


myTuple = (0, 1, False)
print(any(myTuple))
# output: True

mySet = {0, 0, 7}
print(any(mySet))
# output: True

myDict = {0: "Zero", 1: "One"}
print(any(myDict))
# output: True

myList = [0, False, {}, [], (), None]
print(any(myList))
# output: False