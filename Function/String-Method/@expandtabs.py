# Sets the tab size to the specified number of whitespaces

string = "H\te\tl\tl\to"

tabsize = 2
def printLine(string):
    string = string.expandtabs(tabsize)
    print(string.center(51, '!'))
    
for i in range(11):
    printLine(string)
    tabsize += 1

# Output:

# !!!!!!!!!!!!!!!!!!!!!H e l l o!!!!!!!!!!!!!!!!!!!!!
# !!!!!!!!!!!!!!!!!!!H  e  l  l  o!!!!!!!!!!!!!!!!!!!
# !!!!!!!!!!!!!!!!!H   e   l   l   o!!!!!!!!!!!!!!!!!
# !!!!!!!!!!!!!!!H    e    l    l    o!!!!!!!!!!!!!!!
# !!!!!!!!!!!!!H     e     l     l     o!!!!!!!!!!!!!
# !!!!!!!!!!!H      e      l      l      o!!!!!!!!!!!
# !!!!!!!!!H       e       l       l       o!!!!!!!!!
# !!!!!!!H        e        l        l        o!!!!!!!
# !!!!!H         e         l         l         o!!!!!
# !!!H          e          l          l          o!!!
# !H           e           l           l           o!
