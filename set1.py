#!/usr/bin/python

# Collection of multiple items
# Unordered and unindexed
# Items are unique in the set

# set() is a function, in the following example, convert element in the set.
set1 = set((1,2,3))
print ("set1: ", set1)

# In the following example list convert to set.
set_list = set(['a','b','c'])
print ("set_list: ", set_list)

#
# In the following example following multiple element convert to set.
# Added the duplicate element to the set, but in result set display the unique elements.
#
set2 = set((1,'a',2,'c',3,4,4))
print ("set2: ", set2)

string1 = "Python"

# Convert the string into list in ordered.
print ("String convert to list: ", list(string1))

# Convert the string into tuple in ordered.
print ("String convert to tuple: ", tuple(string1))

# Convert the string into string, but display unordered.
print ("String convert to set: ", set(string1))

# For empty set bool() function print the "False"
set3 = set()
print ("Empty set in set3: ", bool(set3))

set4 = set((1,2,3))
print ("Set4 is not empty set: ", bool(set4))

print ("Length of set4: ", len(set4))

# Print in the boolean value.
print (2 in set4)

