#!/usr/bin/python

a = input("Enter the value for a: ")
b = input("Enter the value for b: ")

#
# The != is not qual to. In this example we are checking the variable is not empty.
# If variable is not empty then condition will pass.
# If variable is empty then condition will fail.
# "and": The property of "and" is both condition should be true.
# 
if a != "" and b != "":
    if a > b:
        print ("a: ", a, "\nb: ", b)
        print ("a is greater than b")
    elif a == b:
        print ("a: ", a, "\nb: ", b)
        print ("a is qual to b")
    elif a < b:
        print ("a: ", a, "\nb: ", b)
        print ("b is greater than a")   
else:
    print ("The variable a or b is empty")
