# delete the specified attribute from the specified object

class Person:
    name = 'Wayne'
    age = 69
    country = 'Japan'


print(Person.country)
# out: Japan

delattr(Person, 'country')

print(Person.country)
# out:
#   AttributeError: 
#   type object 'Person' has no attribute 'country'

