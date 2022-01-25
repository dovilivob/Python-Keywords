# getattr(object, attribute, default)
class Person:
    name = 'John'
    age = 79
    country = 'Germen'
    
x = getattr(Person, 'age')
print(x)
# out: 79

attr = 'weight'
y = getattr(Person, attr, 'No attribute called {}'.format(attr))
print(y)
# out:
#   No attribute called weight
