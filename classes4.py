#!/usr/bin/env python3

class Name:

    #
    # The __init__ function initialize complete class OR constructor 
    # The self is the reference of the class
    #
    def __init__(self,name):
        self.name = name
        print ("This is __init__ ",self)

    #
    # The self is the reference of the class
    # Return the value
    #
    def set_name(self):
        return self.name

# Initialize the object
n1 = Name ("Python")

# Print the value
print (n1.set_name()) 
