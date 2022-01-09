# return the specified source as a code object, ready to be executed

# compile(source, filename, mode, flag, dont_inherit, optimize)


x = compile('print(33)', 'test', 'eval')
exec(x)
# output: 33

y = compile('print(55)\nprint(343)', 'test', 'exec')
exec(y)
# output: 
#   55
#   343

z = compile('a=0\nfor i in range(7):\n\tprint(a)\n\ta+=1', 'test', 'exec')
exec(z)
# output:
# 0
# 1
# 2
# 3
# 4
# 5
# 6
