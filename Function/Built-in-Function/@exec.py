# Executes the specified Python code.
# accepts large blocks of code, 
# unlike the eval() which only accepts a single expression

forloop = 'for i in range(7): print(i)'
exec(forloop)

# output:
# 0
# 1
# 2
# 3
# 4
# 5
# 6

printName = 'name = "David"\nprint(name)'
exec(printName)
# output: David