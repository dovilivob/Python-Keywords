# Python program to
# demonstrate static methods

class Maths():

    @staticmethod
    def addNum(num1, num2):
        return num1 + num2


# Driver's code
if __name__ == "__main__":

    # Calling method of class
    # without creating instance
    res = Maths.addNum(1, 2)
    print("The result is", res)

# Output: 
#   The result is 3


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # a static method to check if a Person is adult or not.
    @staticmethod
    def isAdult(age):
        return age > 18


# Driver's code
if __name__ == "__main__":
    res = Person.isAdult(12)
    print('Is person adult:', res)

    res = Person.isAdult(22)
    print('Is person adult:', res)

# Output:
#   Is person adult: False
#   Is person adult: True
