#!/usr/bin/python

# Declaration of list
list1 = ["one", "two", "three", "four", "five"]
print (list1)

# Print the value in 2nd position
print (list1[2])

# Print the index of two
index = list1.index('two')
print ("Index of two: ", index)

print("")

for x in list1:
    print ("The index of ",x,": ",list1.index(x))

# Print the length of list1
print ("Length: ", len(list1))
print ("")

# Replace the value in 2nd postision in list
list1[2] = 10

print (list1)

print("")

# Added a list in 1st position of list1
list1 [1] = [22, 33, 44]

print (list1)

# Print the value of 2nd position 
word = "Python"

print (word[2])

