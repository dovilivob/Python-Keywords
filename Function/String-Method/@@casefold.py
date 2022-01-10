# casefold() is similar to the lower()
# casefold() is stronger, more aggressive,
# meaning that it will find more matches when comparing two strings and both are converted using the casefold()


string = "Hello, And Welcome To My World!"

print(string.casefold())
# Output:
#   hello, and welcome to my world!

print(string.lower())
# Output:
#   hello, and welcome to my world!
