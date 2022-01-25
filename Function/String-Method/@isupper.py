file = open('./@isupper.py', 'a')

def stuff(arr):
    for element in arr:
        print('# ' + element, element.isupper(), sep='\t'.expandtabs(
            15-len(element)), file=file)


arr = list(('HELLO', 'HEY123', 'ay Yo', 'AA BB'))
stuff(arr)

# out:

# HELLO          True
# HEY123         True
# ay Yo          False
# AA BB          True
