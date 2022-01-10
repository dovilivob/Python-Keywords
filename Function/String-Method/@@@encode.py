
string = 'My name is 邱傑義'

(encoding, errors) = ('utf-8', 'ignore')

print(string.encode(encoding="ascii", errors="backslashreplace"))
# b'My name is \\u90b1\\u5091\\u7fa9'

print(string.encode(encoding="ascii", errors="ignore"))
# b'My name is '

print(string.encode(encoding="ascii", errors="namereplace"))
# b'My name is \\N{CJK UNIFIED IDEOGRAPH-90B1}\\N{CJK UNIFIED IDEOGRAPH-5091}\\N{CJK UNIFIED IDEOGRAPH-7FA9}'

print(string.encode(encoding="ascii", errors="replace"))
# b'My name is ???'

print(string.encode(encoding="ascii", errors="xmlcharrefreplace"))
# b'My name is &#37041;&#20625;&#32681;'


# Errors:

# 'backslashreplace' - uses a backslash instead of the character that could not be encoded
# 'ignore' - ignores the characters that cannot be encoded
# 'namereplace' - replaces the character with a text explaining the character
# 'strict' - Default, raises an error on failure
# 'replace' - replaces the character with a questionmark
# 'xmlcharrefreplace' - replaces the character with an xml character
