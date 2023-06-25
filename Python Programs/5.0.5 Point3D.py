# - - - - - - - - - - - - - - - - #
# SummerTech/Coditum Curriculum   #
# Created by Matthew Baptist      #
#                                 #
# Report any bugs, issues, or     #
# corrections to:                 #
# matt@summertech.net             #
#                                 #
#                                 #
# Module 5.0.5                    #
# - - - - - - - - - - - - - - - - #

#SUMMERTECH CONFIDENTIAL
#COPYRIGHT (C) 2017 SUMMERTECH, INC. ALL RIGHTS RESERVED

"""
Teaching Notes:

Goal: Reinforce object oriented programming while introducing
some common patterns more formally. 

Remarks:
1. The motivations of working with points in 3D are intuitively obvious, 
(applications in math, graphics, etc), and the benefits of abstracting 
them into a class can be seen by how easy they are to work with. i.e. 
compare to working with an array of x, y, z values, parallel x/y/z arrays, 
or a 2D array of points.
2. Introduce the __str__ method, this is nearly identical to the toString()
method from before, except Python is built to work with it. This is common
in Python, Java, most languages.
3. Remark: The distance method is a successful abstraction, Point3D objects
are responsible for calculating distances between Point3Ds, programmers
don't have to think about how it is implemented.
"""

from math import sqrt

class Point3D:
  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z

  def __str__(self):
    return "(" + str(self.x) + "," + str(self.y) + "," + str(self.z) + ")"

  def distance(self, other):
    return sqrt( (self.x - other.x)**2 + (self.y - other.y)**2 + (self.z - other.z)**2 )

a = Point3D(0, 0, 0)
b = Point3D(3, 0, 0)
c = Point3D(3, 4, 0)

print(a, b, c)
print(a.distance(b)) #Should equal 3
print(a.distance(c)) #Should equal 5
print(b.distance(c)) #Should equal 4
