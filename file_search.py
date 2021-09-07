#!/usr/bin/env python3

import json

file_name = "data.json"

file_state = open(file_name,"rt")

data = json.load(file_state)

print ("len(data['book']): ",len(data['book']))
print ("\ndata['book'][0]: \n", data['book'][0])
print ("\ndata['book'][1]: \n",data['book'][1])


print (data['book'][0]['id'])
#for r in len(data['book']):
#   if [ data.keys() == 777  ]:
#        print (r)
#   print (r)
