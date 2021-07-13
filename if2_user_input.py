#!/usr/bin/python

# The program compare the variables using sign greater than ">", less than "<" and equal to "=="

a = input("Enter the value for a: ")
b = input("Enter the value for b: ")

if a > b:
    print ("a: ", a, "\nb: ", b)
    print ("a is greater than b")
elif a == b:
    print ("a: ", a, "\nb: ", b)
    print ("a is qual to b")
elif a < b:
    print ("a: ", a, "\nb: ", b)
    print ("b is greater than a")   
