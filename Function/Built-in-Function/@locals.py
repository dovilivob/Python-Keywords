x = locals()

print(x)
# Output:
#   {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x7f805b23dc10>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/dovilivob/Programming/Python-Keywords/Function/Built-in-Function/locals.py', '__cached__': None, 'x': {...}}

print(x['__name__'])
# Output:
#   __main__

print(x['__file__'])
# Output: 
#   /home/dovilivob/Programming/Python-Keywords/Function/Built-in-Function/locals.py
