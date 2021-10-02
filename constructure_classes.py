#!/usr/bin/env python3

import gc 

class Number:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def get_number(self):
        print (self.x," ",self.y)

    def print_number(self, a, b):
        self.a = a
        self.b = b
        print (self.a, " ", self.b )

n1 = Number(10,20)
n1.get_number()

n2 = Number(30)
n2.attr = 5

print (n2.x, n2.y, n2.attr)

n3 = Number()
n3.a1 = 50
n3.b1 = 100
print (n3.a1," ",n3.b1) 

n3.print_number(21,11)

# The del clear the partially memory from the namespace.
del n1
del n2
del n3

#print (n1," ",n2," ",n3)

# Clear all memory used by this program.
n = gc.collect()

print("Number of unreachable objects collected by GC:", n)
print("Uncollectable garbage:", gc.garbage)
