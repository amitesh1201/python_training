#!/usr/bin/env python3
import sys

print ("\n===============Size of integer===============")
num1 = 10
print ("\nSize of integer variable num1: ", sys.getsizeof(num1))

print ("\n===============Size of float===============")
num1 = 1.2
print ("\nSize of float variable num1: ", sys.getsizeof(num1))

print ("\n===============Size of integer list===============")
empty_list = []
print ("\nSize of empty list: ",empty_list,": ", sys.getsizeof(empty_list))

list1 = [1]
print ("\nSize of list: ",list1,": ",  sys.getsizeof(list1))

list1 = [1,2]
print ("\nSize of list: ",list1,": ",  sys.getsizeof(list1))

print ("\n===============Size of string===============")
str1 = ""
print ("\nSize of empty string: ", sys.getsizeof(str1))

str1 = "P"
print ("\nSize of empty string: ", str1,": ", sys.getsizeof(str1))

str1 = "Py"
print ("\nSize of empty string: ", str1,": ",sys.getsizeof(str1))

str1 = "Python"
print ("\nSize of empty string: ",str1, ": ",sys.getsizeof(str1))

print ("\n===============Size of string list===============")
list1 = ['a']
print ("\nSize of list: ",list1,": ",  sys.getsizeof(list1))

list1 = ['a','b']
print ("\nSize of list: ",list1,": ",  sys.getsizeof(list1))

list1 = ['a','b','c']
print ("\nSize of list: ",list1,": ",  sys.getsizeof(list1))

list1 = ['a','b','c','d']
print ("\nSize of list: ",list1,": ",  sys.getsizeof(list1))

print ("\n===============Size of integer tuple===============")
tuple1 = ()
print ("\nSize of empty tuple: ", tuple1,": ", sys.getsizeof(tuple1))

tuple1 = (1)
print ("\nSize of integer tuple: ", tuple1,": ", sys.getsizeof(tuple1))

tuple1 = (1,2)
print ("\nSize of integer tuple: ", tuple1,": ", sys.getsizeof(tuple1))

tuple1 = (1,2,3)
print ("\nSize of integer tuple: ", tuple1,": ", sys.getsizeof(tuple1))

print ("\n===============Size of string tuple===============")

tuple1 = ('a')
print ("\nSize of string tuple: ", tuple1,": ", sys.getsizeof(tuple1))

tuple1 = ('a','b')
print ("\nSize of string tuple: ", tuple1,": ", sys.getsizeof(tuple1))

tuple1 = ('a','b','c')
print ("\nSize of string tuple: ", tuple1,": ", sys.getsizeof(tuple1))
