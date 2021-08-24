#!/usr/bin/env python3

#
# The try-except handles exception (error) in the program and helps to execute \
# the program with a proper error message without any interruption in the program.
# There are two blocks, try and except.
# The try block executes first.
# If there is no exception (error) in the program, then except block skips.
# If there is an exception (error), then except block executes \
# which handles the exception (error) in the program.
#

while True:
     try:
        x = int(input("Please enter a number: "))
        break
     except ValueError:
         print ("You have entered the non-numeric value. Enter the numerical value.")
     except KeyboardInterrupt:
         print ("\nYou have press Ctr + c.")
         exit (1)
