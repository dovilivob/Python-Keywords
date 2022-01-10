# returns True if the specified object is callable
def x():
    a = 5


a = 9


def y(a, b): return a * b


class A:
    a = 78


print(callable(x))
# Output: True

print(callable(8))
# Output: False

print(callable(y))
# Output: True

print(callable(a))
# Output: False

print(callable(A))
# Output: True
