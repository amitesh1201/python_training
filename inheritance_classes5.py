#!/usr/bin/env python3

class Name:

    #
    # The __init__ function initialize complete class OR constructor 
    # The self is the reference of the class
    #
    def __init__(self,name):
        self.name = name

    # The self is the reference of the class
    def set_name(self):
        msg = "The set_name function in class Name" + self.name
        return msg

class Person(Name):
    #
    # The __init__ function initialize complete class OR constructor 
    # The self is the reference of the class
    #
    def __init__(self,name):
        self.name = name
        print ("Print name of class Name", Name)
        print ("\nPrint name of class Name", Person)

    # The self is the reference of the class
    def set_name(self):
        msg = "The set_name function in class Name" + self.name
        return msg


n1 = Name("Python")
print (n1.set_name())

p1 = Person("Java")
print (p1.set_name())
