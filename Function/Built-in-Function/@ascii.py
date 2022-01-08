# ascii(object)
# object: String, List, Tuple, Dictionary, etc...

print(ascii("你好"))
# output: '\u4f60 \u597d'

print(ascii([3, "hello", "你好"]))
# output: [3, 'hello', '\u4f60\u597d']
