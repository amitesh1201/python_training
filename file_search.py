#!/usr/bin/env python3

import json

file_name = "data.json"

file_state = open(file_name,"rt")

data = json.load(file_state)

print (data['book'])
#for r in data:
#   #if [ data.keys() == 777  ]:
#   #     print (r)
#   print (r.keys())
