def stuff(arr):
    for element in arr:
        print(element, element.islower(), sep='\t'.expandtabs(
            20-len(element)), end='\n# ')


arr = list(('hello', 'Okay', '333', 'how are you'))
stuff(arr)

# out:

# hello               True
# Okay                False
# 333                 False
# how are you         True
