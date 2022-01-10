# return a memory view object from asepcified object

# memoryview(obj)
# obj: A Bytes object or a Bytearray object

x = memoryview(b"hello")

print(list(x))
# output:
#   [104, 101, 108, 108, 111]
