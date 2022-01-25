file = open('./@lower.py', 'a')


def stuff(arr):
    for element in arr:
        print('# ' + element, element.lower(), sep='\t'.expandtabs(
            20-len(element)), file=file)


arr = list(('Hello my FRIENDS!', 'ARE YOU OK'))

stuff(arr)

# output:

# Hello my FRIENDS!   hello my friends!
# ARE YOU OK          are you ok
