# Returnss a zip object, which si an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together etc.

# If the fassed iterators have different lengths, the iterator with the least items decides the length of the new iterator

(iterator1, iterator2, iterator3, iterator4) = (
    (1, 4, 5, 3, 53, 2), (1, 42, 5, 2), (42, 55, 52, 53, 11, 0), (4, 22, 53, 2))

x = zip(iterator1, iterator2, iterator3, iterator4)

# use the tuple() function to display a readable version of the result:
print(tuple(x))
# out:
#   ((1, 1, 42, 4), (4, 42, 55, 22), (5, 5, 52, 53), (3, 2, 53, 2))

(name, age) = (['David', 'Wayne', 'Jerry', 'Jackson'], [20, 21, 21, 22])
print(list(zip(name, age)))
# out:
#   [('David', 20), ('Wayne', 21), ('Jerry', 21), ('Jackson', 22)]
