# Returns a bytes object.

# bytes returns an object that cannot be modified,
# bytearry returns an object that can be modified. 

# byte(x, encoding, error)

x = 7
bx = bytes(x)
bax = bytearray(x)

print(bx)
# Output:
#   b'\x00\x00\x00\x00\x00\x00\x00'

print(bax)
# Output:
#   bytearray(b'\x00\x00\x00\x00\x00\x00\x00')

bax[2] = 3

# modifying

print(bax)
# Output:
#   bytearray(b'\x00\x00\x03\x00\x00\x00\x00')
