# Returns True if all the chars are decimals (0 - 9)

def stuff(string):
    result = string.isdecimal()
    print(result)
    
stuff('\u0033') # unicode for '3'

# out: True


stuff('3')

# out: True


stuff('32_32')

# out: False


stuff('\u0030') # 0

# out: True


stuff('\u0047') # G

# out: False


stuff(3232)

# out: 
#   AttributeError: 'int' object has no attribute 'isdecimal'


