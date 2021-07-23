#!/usr/bin/python



list1 = [1,2,3,4,5]

print ("The original list: ", list1)

print ("")
list1.remove(2)
print ("Remove element in the list: ", list1)
print ("Length of list: ", len(list1))

print ("")
# The pop function remove the last element in the list
list1.pop()
print ("Removed last element: ", list1)

print ("")
# The pop function remove element in 1st position in the list
list1.pop(1)
print ("Removed element in  1st position: ", list1) 
