#!/usr/bin/env python3

#
#  The function is the collection of sequence of statements.
#  Instead of repeating the same code/statements in the program,
#  we can create the set of code/statements assign the name to the set call function. \
#  The function reduces the repeated code structure and quickly calls whenever required. 
#  There are types of functions.
#     1. Nonaurgument function: In such functions do not require argument.
#     2. Single or multi-argument function: The functions require single or multiple arguments according to function structure.
#  In any programing language, the user can define the function and use the programmer to define the function.
#  The def keyword used for to define the function.
#

# The print_msg function is the simple nonaurgument function which prints the message.
def print_msg():
    print ("This is the simple function")

# The argument_function requires the argument.
def argument_function(name):
    print ("The name is: ", name)

# The user_input_function requires the argument from the user.
def user_input_function(arg):
    print ("You have entered: ", arg)

# Take the input from the user for addition of two numbers.
def summation(num1, num2):
    sum = int(num1) + int(num2)
    return sum

# The print_result function print the result of any operartion.
def print_result(result):
    print ("Result of the operation: ", result)

# The undefined_arguments function for undefined arguments 
def undefined_arguments(*args):
    for a in args:
       print (a)

#============Funcation Call============
print_msg()
argument_function("Python")

user_input = input ("Enter the string: ")
user_input_function(user_input)

print ("Addition of two numbers.")
num1 = input ("Enter the num1: ")
num2 = input ("Enter the num2: ")

sum = summation(num1, num2)
print_result(sum)


undefined_arguments(1,2,3,4,5)
