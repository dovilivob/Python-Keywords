# Returns True if all the chars are alphanumeric, 
# meaning alphabet letter (a - z) and numbers (0 - 9)


def stuff(string):
    result = string.isalnum()
    print(result)
    
    
stuff('returnTrue42069')
# out: True

stuff('return False')
# out: False
