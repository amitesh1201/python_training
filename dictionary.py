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

# The keys() function displays the all keys in the form of list in the dictionary.
print ("\nThe keys() function displays the all keys in the form of list in the dictionary.")
print ("dict1.keys(): ", dict1.keys())
print ("list(dict1.keys()): ", list(dict1.keys()))

# The values() function displays the all values of keys in the form of list  in the dictionary.
print ("\nThe values() function displays the all values of keys in the form of list  in the dictionary.")
print ("dict1.values(): ", dict1.values())
print ("list(dict1.values()): ", list(dict1.values()))

# The items() function deplays the dictionary itmes in form of tuples in list.
print ("\nThe items() function deplays the disctionary itmes in form of tuples in list.")
print ("dict1.items(): ",dict1.items())
print ("list(dict1.items()): ",list(dict1.items()))

print ("\n============================\n")

key = 1
if key in dict1:
    print (f"The ",key," exist in the dictionary dict1")
else:
    print (f"The ",key," not exist in the dictionary dict1")

print ("\n============================\n")

for key,value in dict1.items():
    print (key,": ", value)
