# Basically the opposite of all()

# any(iterable X)
# if anything in X is not False (0, empty, None, False):
#   return True
# else:
#   return False


myTuple = (0, 1, False)
print(any(myTuple))
# out: True

mySet = {0, 0, 7}
print(any(mySet))
# out: True

myDict = {0: "Zero", 1: "One"}
print(any(myDict))
# out: True

myList = [0, False, {}, [], (), None]
print(any(myList))
# out: False