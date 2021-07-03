#!/usr/bin/python

x = "There are %d types of people." % 10
# The %d for integer, it return the integer
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)
# The %s for string, it returns the string
print (x)
print (y)
# We can also print the above y variable value using the following print function
print ("Those who know", binary, "and those who", do_not)
print()

# The %r for statement, it returns the string and added the single quote
# The %s for statement, it returns the string and no single quote
print ("I said: %r." % x)
print ("I said: %s." % x)
print()
print ("I also said: '%r'." % y)
print ("I also said: '%s'." % y)

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
# The %r used for hilarious variable value which returns the string.

print()
print (joke_evaluation % hilarious)
w = "This is the left side of..."
e = "a string with a right side."

print (w + e)

