#!/usr/bin/env python3

import sys

class Name:

    #
    # The __init__ function initialize complete class OR constructor 
    # The self is the reference of the class
    #
    def __init__(self,name):
        self.name = name
        print ("This is __init__ ",self," ",sys.getsizeof(self.name),"\n")

    #
    # The self is the reference of the class
    # Return the value
    #
    def set_name(self):
        return self.name

# Initialize the object
n1 = Name ("Python")
n2 = Name ("Java")


# Print reference in the n1
print ("\nPrint the reference in ",n1," ",sys.getsizeof(n1))
# Print the value
print (n1.set_name())

# Print reference in the n2
print ("\nPrint the reference in ",n2," ",sys.getsizeof(n2))
# Print the value
print (n2.set_name())
