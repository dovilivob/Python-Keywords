# Returns True if all the chars are decimals (0 - 9)

def doThings(string):
    result = string.isdecimal()
    print(result)
    
doThings('\u0033') # unicode for '3'

# Output: True


doThings('3')

# Output: True


doThings('32_32')

# Output: False


doThings('\u0030') # 0

# Output: True


doThings('\u0047') # G

# Output: False


doThings(3232)

# Output: 
#   AttributeError: 'int' object has no attribute 'isdecimal'


