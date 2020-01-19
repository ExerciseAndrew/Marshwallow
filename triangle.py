import math
# import time
# import main

# def count():
#     i==0        ##set count to zero for start of game. #Count keeps track of turns.

#start
#scalene triangle sides all different
#isosceles two sides same
#equilateral all sides same

math.pi
a = int(input("The length of side a = \n"))   
b = int(input("The length of side b = \n")) 
c = int(input("The length of side c = \n"))  
r = a + b + c
if a != b and b!=c and a!= c:
    print ("You have chosen Scalene\n")
elif a == b and b == c and a ==c:
    print ("You have chosen Equilateral\n")
else:
    print ("You have chosen Isosceles\n")
def volume(r):  
    """returns the value of a sphere with radius r."""
    v = (4.0/3.0) * math.pi * r**3
    print ("If we line up the sides of your triangle end to end\nand use it as the radius of a sphere, our sphere's volume is\n" +v+ "\n")

#     return v
# if (input("Imagine a sphere. What is its radius?\n>>>")):
#  print ("Do not use words.\n")
#  else:
#      return v

