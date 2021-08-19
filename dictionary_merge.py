#!/usr/bin/env python3

dict1 = {1: 'a', 2: 'b'}
dict2 = {2: 'c', 3: 'd'}
dict3 = {1: 'A', 2: 'B'}
dict4 = {3: 'C'}

print ("dict1: ", dict1)
print ("dict2: ", dict2)
dict1.update(dict2)
print ("The update function merge the two dictionaries and keeps unique values.")
print ("dict1.update(dict2): ", dict1)


print ("\n==========================\n")
print ("dict3: ", dict3)
print ("dict4: ", dict4)
dict3.update(dict4)
print ("dict3.update(dict4): ", dict3) 
