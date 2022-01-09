# all(iterable X)
# iterable: list, tuple, dictionary

# if 0, empty iterable, None, False in X:
#   return False
# else:
#   return True

myList = [True, "thanks", True]
print(all(myList))
# ouptut: True

myList = []
print(all(myList))
# output: True

myList = [[]]
print(all(myList))
# output: False

myList = [00, 33]
print(all(myList))
# output: False

myDict = {0: "Zero", 1: "One"}
print(all(myDict))
# output: False

myDict = {1: "Zero", 2: "One"}
print(all(myDict))
# output: True
