
string = 'banana'
(length, character) = (len(string) + 2 * 4, ' ')

print(string.center(length, character))
# out:
#        banana

character = '_'
print(string.center(length, character))
# out:
#    ____banana____
