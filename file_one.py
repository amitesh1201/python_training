#!/usr/bin/env python3


# If user input is empty or string then handle the condition and print message with exit

import file_two

def fn1():
    print ("The fn1 function is defined in {}" .format(__name__))

def print_message():
    print ("Re-run the programe and enter (1/2)")

def user_input():
    u_input = int(input("Enter the number (1/2)"))
    print ("u_input: ", u_input)
    if u_input == 1:
        file_two.fn()
    elif u_input == 2:
         fn1()
    else:
         print_message()


user_input()
