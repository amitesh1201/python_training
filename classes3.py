#!/usr/bin/env python3

class Name:

    #
    # The __init__ function initialize complete class OR constructor 
    # The self is the reference of the class
    #
    def __init__(self,name):
        self.name = name
        print ("This is __init__ ",self)

    # The self is the reference of the class
    def print_name(self):
        print ("This is print_name function ", self)
        print (self.name)

# initialize the object
n1 = Name ("Python")
# Print the reference of the class
n1.print_name() 
