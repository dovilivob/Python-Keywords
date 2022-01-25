# Returns the global symbol table as a dictionary
# A symbol table contains necessary information about the current program

x = globals()
print(x)
# out:
#   {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x7f9bc212cc10>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/dovilivob/Programming/Python-Keywords/Function/Built-in-Function/globals.py', '__cached__': None, 'x': {...}}

print(x['__file__'])
# out:
#   /home/dovilivob/Programming/Python-Keywords/Function/Built-in-Function/globals.py
