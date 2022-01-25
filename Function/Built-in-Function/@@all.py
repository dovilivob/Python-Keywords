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
# out: True

myList = [[]]
print(all(myList))
# out: False

myList = [00, 33]
print(all(myList))
# out: False

myDict = {0: "Zero", 1: "One"}
print(all(myDict))
# out: False

myDict = {1: "Zero", 2: "One"}
print(all(myDict))
# out: True
