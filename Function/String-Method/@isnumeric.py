def stuff(arr):
    for element in arr:
        print(element, element.isnumeric(), sep='\t'.expandtabs(
            10-len(element)), end='\n# ')


arr = list(('02395', 'one two', '3,4', '3 9', '-1',
           '6.9', '\u0030', '\u00B2', '20km2'))
stuff(arr)

# out:

# 02395     True
# one two   False
# 3,4       False
# 3 9       False
# -1        False
# 6.9       False
# 0         True
# ²         True
# 20km2     False
