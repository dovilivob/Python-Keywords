# classmethod(function)

# classmethod() is considered un-Pythonic,
# so in newer Python versions,
# you can use the @classmethod decorator for classmethod definition

# @classmethod
# def func(cls, args...)

from datetime import date


class Student:
    marks = 0

    def compute_marks(self, obtained_marks):
        marks = obtained_marks
        print('obtained Marks', marks)


Student.print_marks = classmethod(Student.compute_marks)
Student.print_marks(87)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def fromFatherAge(name, fatherAge, fatherPersonAgeDiff):
        return Person(name, date.today().year - fatherAge + fatherPersonAgeDiff)

    @classmethod
    def fromBirthYear(cls, name, birthYear):
        return cls(name, date.today().year - birthYear)

    def display(self):
        print(self.name + "'s age is: " + str(self.age))

class Man(Person):
    sex = 'Male'

person = Person('Adam', 17)
person.display()

otherPerson = Person.fromBirthYear('John', 1998)
otherPerson.display()

man = Man.fromBirthYear('Jerry', 1992)
print(isinstance(man, Man))

otherMan = Man.fromFatherAge('David', 1977, 20)
print(isinstance(otherMan, Man))