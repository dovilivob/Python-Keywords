# getattr(object, attribute, default)
class Person:
    name = 'John'
    age = 79
    country = 'Germen'
    
x = getattr(Person, 'age')
print(x)
# Output: 79

attr = 'weight'
y = getattr(Person, attr, 'No attribute called {}'.format(attr))
print(y)
# Output:
#   No attribute called weight
