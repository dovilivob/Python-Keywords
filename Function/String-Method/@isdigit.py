def stuff(string):
    result = string.isdigit()
    print(result)
    

a = '\u0030'  # 0
b = '\u00B2'  # ²


stuff(a)
# out: True

stuff(b)
# out: True

stuff('hello')
# out: False