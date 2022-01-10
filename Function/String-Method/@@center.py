
string = 'banana'
(length, character) = (len(string) + 2 * 4, ' ')

print(string.center(length, character))
# Output:
#        banana

character = '_'
print(string.center(length, character))
# Output:
#    ____banana____
