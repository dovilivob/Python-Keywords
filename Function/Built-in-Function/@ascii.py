# ascii(object)
# object: String, List, Tuple, Dictionary, etc...

print(ascii("你好"))
# Output: '\u4f60 \u597d'

print(ascii([3, "hello", "你好"]))
# Output: [3, 'hello', '\u4f60\u597d']
