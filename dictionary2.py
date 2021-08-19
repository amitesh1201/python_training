#!/usr/bin/env python3


dict1 = {1: 'Maharastra', 2: 'Kashmir', 3: 'Gujrat'}

print ("\ndict1: ", dict1)

print ("\n=====================\n")
print ("The copy function refer fresh copy of dict2 dictionary\nThe change in dict2 dictionary does not reflects in dict1 dictionary.")
dict2 = dict1.copy()
print ("dict2 = dict2.copy(): ", dict2)
dict2[4] = 'Panjab'
print ("dict2[4] = 'Panjab'", dict2)

print ("\n=====================\n")
print ("\nThe alias refer the copy of dict1 dictionary.\nThe change in alias reflects in dict1 dictionary.")
alias = dict1
print ("alias = dict1: ", alias)

print ("\n=====================\n")
alias[4] = 'Chennai'
print ("\nalias[4] = 'Chennai': ", alias)
print ("\n=====================\n")

print ("Display dict1 after append in the alias: ", dict1)


