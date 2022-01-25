# Returns True if the specified object is of the specified type, otherwise False.
# If the type parameter is a tuple, return True if the object is one the types in the tuple.

print(isinstance(3, int))
# out: True

print(isinstance('Hello', (float, int, list, dict, tuple)))
# out: False

print(isinstance('Hello', (float, int, list, dict, tuple, str)))
# out: True

class Obj:
    name = 'Nick'
    
y = Obj()

print(isinstance(y, Obj))
# out: True

y = 'djfkd'
print(isinstance(y, Obj))
# out: False