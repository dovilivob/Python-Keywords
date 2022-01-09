# return a type containing teh quotioent and the remainder 
# when argument 1 (diviend) is divided by argument 2 (divisor).

# divmod(dividend, divisor) = (quotient, remainder)

dividend = 65
divisor = 9

x = divmod(dividend, divisor)

quotient = x[0]
remainder = x[1]

print(x, quotient * divisor + remainder)

# output:
# (7, 2) 65