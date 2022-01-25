
def doThings(string):
    result = string.isascii()
    print(result)

doThings('David Chiu 0818')

# Output: True

doThings('!!!')
# Output: True

doThings('你好')
# Output: False
