# Used to give access to methods 
# and properties of a parent sibling class.

class Parent:
    def __init__(self, text):
        self.message = text

    def printmessage(self):
        print(self.message)


class Child(Parent):
    def __init__(self, text):
        super().__init__(text)


x = Child("Hello, Welcome!")

x.printmessage()
# output: 
#   Hello, Welcome!
