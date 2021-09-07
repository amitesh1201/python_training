#!/usr/bin/env python3

#
# Create data.json file from the following json file contain  
# The "data.json" file name used in this program. You can create file with different  
# name instead of "data.json" file name and change the same file name in this program.
#{
#   "book":[
#      {
#         "id":"444",
#         "language":"C",
#         "edition":"First",
#         "author":"Dennis Ritchie "
#      },
#      {
#         "id":"555",
#         "language":"C++",
#         "edition":"second",
#         "author":" Bjarne Stroustrup "
#      }
#   ]
#} 

#
# Task:
# 1. Take the "id" input from user, search and display the complete record.
# 2. If the input is other than an integer, then display the proper error message and provide 
# the two more attempts (including the first attempt, means three attempts) to
# the user. 
# 3. If user fail to enter the integer in three attempts then exit the program with proper message.
# 4. If entered input not found then exit with proper message.
# 5. If entered input found then display the complete record and exit with proper message.  
# 6. Create the funtion required tasks.
#

import json


flag = 0
file_name = "data.json"

# Open the file in read format.
file_state = open(file_name,"rt")

# Load the complete file into variable in dictionary format with nested pattern.
data = json.load(file_state)
print ("#########################")
print (data)
print ("#########################\n")

# Get the length of the book data set
print ("len(data['book']): ", len(data['book']))

# Display the first and second record individually.
print ("\nDictionary data['book'][0]: ", data['book'][0])
print ("\nDictionary data['book'][1]: ", data['book'][1])


print ("\ndata['book'][0]['id']: ", data['book'][0]['id'])
len_data = len(data['book']) 
print ("\nlen_data: ", len_data)

for len_d in range(0,len_data):
   print ("\ndata['book'][len_d]['id']: ", data['book'][len_d]['id'])
   if 555 == int(data['book'][len_d]['id']):
       flag = 1


if flag == 1:
   print ("\nRecord found")
   exit (0)


print ("\nRecord not found")

# Close the file after operations.
file_state.close()
