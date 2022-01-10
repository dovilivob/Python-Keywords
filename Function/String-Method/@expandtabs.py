# Sets the tab size to the specified number of whitespaces

string = "H\te\tl\tl\to"

tabsize = 2

print(string.expandtabs(tabsize))
tabsize += 1
print(string.expandtabs(tabsize))
tabsize += 1
print(string.expandtabs(tabsize))
tabsize += 1
print(string.expandtabs(tabsize))
tabsize += 1
print(string.expandtabs(tabsize))
tabsize += 1
print(string.expandtabs(tabsize))
tabsize += 1
print(string.expandtabs(tabsize))

# Output:

# H e l l o
# H  e  l  l  o
# H   e   l   l   o
# H    e    l    l    o
# H     e     l     l     o
# H      e      l      l      o
# H       e       l       l       o
