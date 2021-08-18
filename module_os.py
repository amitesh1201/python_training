#!/usr/bin/python

import os

#
# os.listdir("directory_path") require input as directory path. 
# This function display list of files and directories in the specifies path.
#
list_dir = os.listdir("/")
print ("List of directories and file:\n " , list_dir, "\n")

create_dir = "test-dir"

# The os.makedirs("direcotry_name") function creats the directory
os_create_dir = os.makedirs(create_dir)

print (os_create_dir)
print ("Checks the direcory exists or not (True/False): ", os.path.isdir(create_dir))
print ("Checks the /python_training/one.py file exist or not (True/False): ", os.path.isfile("/python_training/one.py"))
# The os.getcwd() function displays the current working directory
print (os.getcwd())

# The os.chdir("existing_direcotry_name") function change director. 
os.chdir("/")
print (os.getcwd())
