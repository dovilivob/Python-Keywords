
def stuff(string):
    result = string.isascii()
    print(result)

stuff('David Chiu 0818')

# out: True

stuff('!!!')
# out: True

stuff('你好')
# out: False
