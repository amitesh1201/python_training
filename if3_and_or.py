#!/usr/bin/python

num1 = input("Enter the num1: ")
num2 = input("Enter the num2: ")


if num1 != "" and num2 != "":
    print ("The num1 ", num1, "and num2 ", num2, "are not empty")
elif num1 != "" or num2 != "":
    print ("The num1 ", num1, "or num2 ", num2, "is empty")
else:
    print ("The num1 ", num1, "and num2 ", num2, "are empty")

