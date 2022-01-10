# return the __dic__ attribute of an object

# Calling the vars() without parameters will return
# a dictionary containing the local symbol table.

class Person:
    name = 'David'
    age = 21
    country = 'Taiwan'


object = Person

print(vars(Person))

# Output:
#   {'__module__': '__main__', 'name': 'David', 'age': 21, 'country': 'Taiwan', '__dict__': <attribute '__dict__' of 'Person' objects>, '__weakref__': <attribute '__weakref__' of 'Person' objects>, '__doc__': None}

print(vars())
# Output:
#   {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x000002172AA45780>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'vars.py', '__cached__': None, 'Person': <class '__main__.Person'>, 'object': <class '__main__.Person'>}
