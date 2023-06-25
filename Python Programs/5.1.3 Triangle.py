# - - - - - - - - - - - - - - - - #
# SummerTech/Coditum Curriculum   #
# Created by Matthew Baptist      #
#                                 #
# Report any bugs, issues, or     #
# corrections to:                 #
# matt@summertech.net             #
#                                 #
#                                 #
# Module 5.1.3                    #
# - - - - - - - - - - - - - - - - #

#SUMMERTECH CONFIDENTIAL
#COPYRIGHT (C) 2017 SUMMERTECH, INC. ALL RIGHTS RESERVED

from Shape import Shape
from Point3D import Point3D

"""
Teaching Notes:

Goal: Reinforce the concept of derived classes. Implement all
abstract methods.

Remarks:
1. You can start by copy and pasting rectangle
2. Assume that the triangle is right, and that the
points are entered in the following order:

A
|\
| \
B--C

Area is then 1/2 * a.distance(b) * b.distance(c)
Perimeter is the sum of each sides distance
a.distance(c) + a.distance(b) + b.distance(c)
"""

class Triangle(Shape):
  
  def __init__(self, a, b, c):
    self.vertices = [a, b, c]
  
  def __str__(self):
    result = ""
    for i in self.vertices:
      result += str(i) + ","
    result = result[:-1]
    
    return "Triangle: " + result
  
  def getArea(self):
    a = self.vertices[0]
    b = self.vertices[1]
    c = self.vertices[2]
    
    sideA = a.distance(b)
    sideB = b.distance(c)
    
    return 1/2 * sideA * sideB
  
  def getPerimeter(self):
    a = self.vertices[0]
    b = self.vertices[1]
    c = self.vertices[2]
    
    sideA = a.distance(c)
    sideB = a.distance(b)
    sideC = b.distance(c)
    
    return sideA + sideB + sideC

a = Point3D(0, 1, 0)
b = Point3D(0, 0, 0)
c = Point3D(1, 0, 0)

triangle = Triangle(a, b, c)

print(triangle)
print(triangle.getVertices())
print(triangle.getNumVertices())
print(triangle.getArea()) #should be 1/2
print(triangle.getPerimeter()) #should be ~3.4142
