# Returnss True if the specified object is callable
def x():
    a = 5


a = 9


def y(a, b): return a * b


class A:
    a = 78


print(callable(x))
# out: True

print(callable(8))
# out: False

print(callable(y))
# out: True

print(callable(a))
# out: False

print(callable(A))
# out: True
