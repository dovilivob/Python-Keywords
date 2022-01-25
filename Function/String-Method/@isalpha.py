def stuff(string):
    result = string.isalpha()
    print(result)
    
stuff('this is a sentense')
# out: False

stuff('abcdefblablabla')
# out: True