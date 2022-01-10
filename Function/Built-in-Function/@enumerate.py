# Takes a collection and returns it as an enumerate object.
# Adds a counter as the key of the enumerate object.


# enumerate(iterable, start)
# start: A Number. Defining the start number of the enumerate object. Default 0.

x = ('apple', 'banana', 'cherry')
print(enumerate(x))

x = ('hello', 9)
print(enumerate(x))

y = x
print(enumerate(y))
# Output: 
#   <enumerate object at 0x7fa448522a40>
#   <enumerate object at 0x7fa448522a40 >
#   <enumerate object at 0x7fa448522a40 >
