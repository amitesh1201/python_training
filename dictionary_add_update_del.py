#!/usr/bin/env python3

dict1 = {1: 'A', 2: 'B', 3: 'C'}

dict1[4] = 'E'
print ("Add the key pair:\n")
print ("dict1[4] = 'E':\n")
print (dict1)

print ("\n================\n")
dict1[3] = 'F'
print ("Replace the value:\n")
print ("dict1[3] = 'F':\n")
print (dict1)

print ("\n================\n")
del dict1[2]
print ("Delete the key pair:\n")
print ("del dict1[2]\n")
print (dict1)


print ("\n================\n")
print ("Empty dict1 dictionary:\n")
dict1.clear()
print ("dict1.clear(): ", dict1)

