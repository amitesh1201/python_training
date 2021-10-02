#!/usr/bin/env python3

class Name:

    # The __init__ function initialize complete class OR constructor 
    def __init__(self,name):
        self.name = name
        print(self.name, "This is __init__ function with reference self")

# initialize the object
n1 = Name ("Python")
