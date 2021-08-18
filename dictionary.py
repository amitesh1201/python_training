#!/usr/bin/env python3

#
# The dictionary is a collection of ordered items, and it can be changeable. 
# Also, it does not allow duplicates.
# In the dictionary, items are in key:value pair.
#

# The dict1 is a dictionary defined in key:value pair.
dict1 = {1: 'one', 2: 'two', 3: 'three'}
print ("dict1: \n", dict1)

print ("\ndict1[1]: ", dict1[1])

print ("\ndict1[2]: ", dict1[2])

print ("\ndict1.get(3): ", dict1.get(3))

# The following statement raised error, the number 4 is not exists.
# print ("\ndict1[4]: ", dict1[4])

#
# The get() function handles the above condition
# If the value not exists, then it prints the none
# Such types of conditions handled in dynamic programing
#
print ("\ndict1.get(4): ", dict1.get(4))
