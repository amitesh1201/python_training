#!/usr/bin/python


list1 = ["one", "two", "three"]
print ("Original list: ", list1)
print ("")
# Insert funtion requires two arguments first is index and second is value
list1.insert(0, "zero")
print ("Insert element in 0th position: ", list1)
print ("Length of list: ", len(list1))

print ("")
list1.insert(2, "3")
print ("Insert element in 2nd list: ", list1)
print ("Length of list: ", len(list1))

print ("")
list1.insert(-1, 4)
print ("Insert element in -1(last) position: ", list1)
print ("Length of list: ", len(list1))

print ("")
list1[0:0] = [1,2,3]
print ("Insert element in the 0:0 position: ", list1)
print ("Length of list: ", len(list1))

print ("")
# The list1[0:3] = ["a", "b", "c"] list replace the a,b,c with all first 3 element in list 
list1[0:3] = ["a", "b", "c"]
print ("Insert element in the 0:3 position", list1)
print ("Length of list: ", len(list1))


print ("")
list1.append("four")
print ("Append element in list: ", list1)
print ("Length of list: ", len(list1))

print ("")
list1.remove("two")
print ("Remove element in the list: ", list1)
print ("Length of list: ", len(list1))

# Remove the element in particular position
