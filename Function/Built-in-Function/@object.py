# return an empty object
# You cannot add new properties or methods to this object
# This object is the base for all classes, 
# it holds the built-in properties and methods 
# which are default for all classes.


x = object()
print(dir(x))
# Output:
#   ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
