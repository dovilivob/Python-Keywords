def stuff(arr):
    for element in arr:
        print('# ' + element, element.isspace(), sep='\t'.expandtabs(
            10-len(element)))


arr = list(('   ', ' ', '   d   ', ' '.center(5, ' ')))
stuff(arr)

# out:

#           True
#           True
#    d      False
#           True
