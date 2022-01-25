# Formats a specified value into a specified format

# format(value, format)


print(format(0.3434, '%'))
# out:
#   34.340000%

print("{0} {1} {1} {2}".format("hello", "world", "NiHow"))
# out:
#   hello world world NiHow

name = "Tom"
age = 89
string = 'My name is {} and my age is {}'.format(name, age)
print(string)
# out:
#   My name is Tom and my age is 89

print("{:>10}".format('hello'))
# out:
#      hello

print('{:,}'.format(3838383298232))
# out:
#   3,838,383,298,232

print('{} {} {} {} {} {} {}'.format(*'1234567'))
# out:
#   1 2 3 4 5 6 7

print('The student is {students[1]}'.format(
    students=['David', 'Jerry', 'Wayne']))
# out:
#   The student is Jerry

# To format dict, add ** before the dict object
print('My age is {age} and gender is {gender}'.format(
    **{'age': 20}, **{'gender': "Male"}))
# out:
#   My age is 20 and gender is Male


# '<' - Left aligns the result(within the available space)
# '>' - Right aligns the result(within the available space)
# '^' - Center aligns the result(within the available space)
# '=' - Places the sign to the left most position
# '+' - Use a plus sign to indicate if the result is positive or negative
# '-' - Use a minus sign for negative values only
# ' ' - Use a leading space for positive numbers
# ',' - Use a comma as a thousand separator
# '_' - Use a underscore as a thousand separator
# 'b' - Binary format
# 'c' - Converts the value into the corresponding unicode character
# 'd' - Decimal format
# 'e' - Scientific format, with a lower case e
# 'E' - Scientific format, with an upper case E
# 'f' - Fix point number format
# 'F' - Fix point number format, upper case
# 'g' - General format
# 'G' - General format(using a upper case E for scientific notations)
# 'o' - Octal format
# 'x' - Hex format, lower case
# 'X' - Hex format, upper case
# 'n' - Number format
# '%' - Percentage format


# f-string
name = 'Wayne'
job = 'Orphan'
string = f"My name is {name} and my job is being an {job}"
print(string)
# out:
#   My name is Wayne and my job is being an Orphan

print(f"A total number of {10* 339 + 334}")
# out:
#   A total number of 3724

print(f"convert ASSHOLE to lower words: {'ASSHOLE'.lower()}")
# out:
#   convert ASSHOLE to lower words: asshole

print(f"Complex Number {(2 + 8j) / (4 - 7j)}")
# out:
#   Complex Number (-0.7384615384615386+0.7076923076923077j)

men = ['David', 'Jerry', 'Wayne']
print(f"Get the second man: {men[1]}")
# out:
#   Get the second man: Jerry

desableSpecialChar = rf"\n\n\n\n\n\t\t\\\\"
print(desableSpecialChar)
# out:
#   \n\n\n\n\n\t\t\\\\

num = 478394.8383

print(f'num is {num:f}')
# out:
#   num is 478394.838300

print(f'num is {num:,f}')
# out:
#   num is 478,394.838300


print(f"""even ? ansewr: {(lambda n : "Yes" if n % 2 == 0 else "No") (11)}""")
# out:
#   even ? enswer: No