# lambda
print((lambda x, y: x * y)(4, 2))

mult = lambda x, y: x * y

# def mult(x, y):
#     return x * y

print(mult(4, 9))


# filter()
numbers = [3, 24, 43, 55, 5, 63, 66, 73]

result = filter(lambda x: x > 10, numbers)
print(list(result))


# map
result = map(lambda x: x / 2, numbers)
print(list(result))


# reduce
from functools import reduce

numbers = [33, 44, 11]
result = reduce(lambda x, y: x + y, numbers)
print(result)


# sorted
cars = [
    ("Mazda", 2000),
    ("Toyota", 1000),
    ("Benz", 5000),
]

# import json
# jsonCars = json.loads(cars)
# print(jsonCars)


print(type(cars[1]))

print(sorted(cars, key=lambda car: car[1]))
