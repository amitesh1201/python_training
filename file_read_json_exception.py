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

#  This programe read the json file.
#  Also, checks user input file exist or not, file is json or not. 
#  If user press Ctrl + c then handle the action.
#


import json, os

def check_file_exist(fname):
    try:
        # The following statement open the file read text mode       
        file_state = open(fname,"rt")
        data = json.load(file_state)
    except ValueError:
        print ("The file",fname,"is not a json file.")
        exit (1)
    except FileNotFoundError:
        print ("The file",fname,"not exist.")
        exit (1)

    print (data)
    file_state.close()


def filename_userinput():
    try:
        file_name = input ("Enter the filename including complete path: ")
    except KeyboardInterrupt:
         print ("\nYou have press Ctr + c.")
         exit (1)
     
    check_file_exist (file_name)

# ============ Function call ============
filename_userinput()
