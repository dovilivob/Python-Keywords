from os import sep

# object(s)	
#   Any object, and as many as you like. Will be converted to string before printed

# sep = 'separator'	
#   Optional. Specify how to separate the objects, if there is more than one. Default is ' '

# end = 'end'	
#   Optional. Specify what to print at the end. Default is '\n' (line feed)

# file	
#   Optional. An object with a write method. Default is sys.stdout

# flush	
#   Optional. A Boolean, specifying if the Output is flushed(True) or buffered(False). Default is False

string1, string2 = 'Hello', 'how are you?'


class vars: (separator, end, file, flush) = (' ', '\n', 'sys.stdout', False)

(separator, end, file, flush) = vars.separator, vars.end, vars.file, vars.flush

print(string1, string2, sep=separator, end=end, flush=flush)
# Output: 
#     Hello how are you?

file = open('./data/printFile.txt', 'w')
separator, end, flush = ' --- ', ' ### This is the end of the line!', False

print(string1, string2, sep=separator, end=end, file=file, flush=flush)
# Output:
#   (In the text file)
#   Hello --- how are you? ### This is the end of the line!