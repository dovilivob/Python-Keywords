# setattr(object, attribute, value)
class Person:
    name = 'David'
    age = 21
    country = 'Taiwan'
    
setattr(Person, 'job', 'student')

print(Person.job)