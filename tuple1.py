#!/usr/bin/python


tuple1 = (1,2,3,4,5)

print ("Integer Tuple: ", tuple1)

print ("")

tuple2 = (1, "python", 2, "liux")

print ("Mix Tuple2: ", tuple2)
print ("len(tuple2): ", len(tuple2))
print ("tuple2[1]: ", tuple2[1])
print("tuple2[row][column] tuple2[1][0]: ", tuple2[1][0])

#
# The tuple3 is combination of integer, list and tuple. This tuple is nested.
# In this tuple we can change the value in list ['a','b','c'] but cannot change value of tuple (1,2,3,4,5)
#
print ("")
tuple3 = (1,['a','b','c'],(1,2,3,4,5))
print ("Nested Tuple3: ", tuple3)
print ("len(tuple3): ", len(tuple3))
print ("tuple3[1][0]: ", tuple3[1][0])
print ("tuple3[1][1]: ", tuple3[1][1])
print ("tuple3[2][1]: ", tuple3[2][1])
tuple3[1].append('d')
print ("Nested Tuple3 tuple3[1].append('d'): ", tuple3)

print("")
#
# In the following statement, we can not change the value. tuple3[2][0] in this position of tuple there is another tuple which is nested.
# You can remove the # infront of line and run program, it gives you an error.
#
#tuple3[2][0] = 0
#print ("Nested Tuple3: ", tuple3)

tuple3[1][0] = 0
print ("Nested Tuple3: ", tuple3)

tuple3[1][0] = "" 
print ("Nested Tuple3: ", tuple3)

print ("")
tuple4 = ('a','e','i','o','u')
print ("Tuple4: ", tuple4)
print ("tuple4[-1]: ",tuple4[-1])
print ("tuple4[-3]: ",tuple4[-3])

print("")
print("tuple4[3:]: ", tuple4[3:])
print("tuple4[:4]: ", tuple4[:4])
print("tuple4[2:5]: ", tuple4[2:5])
print("tuple4[:]: ", tuple4[:])


print ("")
tuple5 = ('a','e','e','i','o','u')
print ("Tuple5: ", tuple5)
print ("tuple5.count('e'): ",tuple5.count('e'))
print ("tuple5.index('i'): ",tuple5.index('i'))
print ("a in tuple5: ", 'a' in tuple5)
print ("q in tuple5: ", 'q' in tuple5)

print ("")
print ("Print tuple using for loop")
for tuple in tuple5:
    print (tuple)
