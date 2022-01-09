# returns True if the specified object is callable
def x():
    a = 5


a = 9


def y(a, b): return a * b


class A:
    a = 78


print(callable(x))
# output: True

print(callable(8))
# output: False

print(callable(y))
# output: True

print(callable(a))
# output: False

print(callable(A))
# output: True
