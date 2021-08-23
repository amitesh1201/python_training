#!/usr/bin/env python3

#
# In this program, we defined the default value for the function.
# If the user provides the argument to the function, then the function print/returns the value.
# If the user does not provide the argument to the function, \
# then the default defined assigns to the variable in the function, and print/returns the value.
#


def default_value_function(language = "Python"):
    print ("You have entered ", language, " language")



default_value_function("C")
default_value_function("C++")
# The following function call print the defualt value in the function.
default_value_function()
default_value_function("Java")
default_value_function("Ruby")
