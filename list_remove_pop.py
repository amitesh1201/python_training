#!/usr/bin/python



list1 = [1,2,3,4,5]

print ("The original list: ", list1)

print ("")
list1.remove(2)
print ("Removed element 2 in the list: ", list1)
print ("Length of list: ", len(list1))

print ("")
# The pop function remove the last element in the list
list1.pop()
print ("Removed last element: ", list1)

print ("")
# The pop function remove element in 1st position in the list
element = list1.pop(1)
print ("Removed element in  1st position: ", list1) 
print ("Popup element in the list: ", element)

# The del method delete the element in the 1st position in the list
del list1[1]
print ("Deleted the element in list: ", list1)

print ("")
# The clear function remove all elements in the list
list1.clear()
print ("Removed all elements: ", list1)

print ("")
list2 = ['a', 'b', 'c']
print ("The oiginal list2 list: ", list2)

print ("")
# Remove all element in the list
del list2[:]
print ("Removed all element in the list: ", list2)

print ("")
# Delete the complete list 
del list2
print (list2)
