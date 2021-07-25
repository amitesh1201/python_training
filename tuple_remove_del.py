#!/usr/bin/python

#
# We cannot remove elements  in tuple. Convert tuple to list and update the list.
# Covert list to tuple.
#
tuple1 = (1,2,3,4)
print ("tuple1: ", tuple1)

list1 = list(tuple1)

list1.remove(2)

tuple1 = tuple(list1)

print ("Removed element in tuple: ", tuple1)
