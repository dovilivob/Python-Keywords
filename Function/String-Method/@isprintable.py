def stuff(arr):
    for element in arr:
        print('# ' + element, element.isprintable(), sep='\t'.expandtabs(
            20-len(element)))


arr = list(('Hello! Are you @1?', 'fuck', 'Hello! Are you \t@1?'.expandtabs(1), 'ok\n\b\t'))
stuff(arr)

# out:

# Hello! Are you @1?  True
# fuck                True
# Hello! Are you  @1? True
# ok
#                        False
