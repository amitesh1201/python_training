#!/usr/bin/env python3

import json


flag = 0
file_name = "data.json"

file_state = open(file_name,"rt")

data = json.load(file_state)

print ("len(data['book']): ", len(data['book']))
print ("\ndata['book'][0]: \n", data['book'][0])
print ("\ndata['book'][1]: \n", data['book'][1])


print (data['book'][0]['id'])
len_data = len(data['book']) 
print ("len_data: ", len_data)

for len_d in range(0,len_data):
   print ("data['book'][len_d]['id']: ", data['book'][len_d]['id'])
   if 555 == int(data['book'][len_d]['id']):
       flag = 1


if flag == 1:
   print ("Record found")
   exit (0)


print ("Record not found")
