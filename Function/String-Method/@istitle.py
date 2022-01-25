# Title means that the string is start with a upper letter, 
# AND the rest of the word are lower case


def stuff(arr):
    for element in arr:
        print('# ' + element, element.istitle(), sep='\t'.expandtabs(
            15-len(element)))


arr = list(('Hello', 'HeLLo', '!!!DDD', 'Gay69', 'A!@#$%^&^"'))
stuff(arr)

# out:

# Hello          True
# HeLLo          False
# !!!DDD         False
# Gay69          True
# A!@#$%^&^"     True
