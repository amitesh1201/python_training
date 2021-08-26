#!/usr/bin/env python3

#
# The following different types of file mode in python
# 'r'     open for reading (default)
# 'w'     open for writing, truncating the file first
# 'x'     open for exclusive creation, failing if the file already exists
# 'a'     open for writing, appending to the end of the file if it exists
# 'b'     binary mode
# 't'     text mode (default)
# '+'     open a disk file for updating (reading and writing)
# 'U'     universal newlines mode (deprecated)
#

import json

file_name="data.json"

# The following statement open file in read text mode.
file_state = open(file_name,"rt")
data = json.load(file_state)

print (data) 


