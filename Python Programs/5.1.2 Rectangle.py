# - - - - - - - - - - - - - - - - #
# SummerTech/Coditum Curriculum   #
# Created by Matthew Baptist      #
#                                 #
# Report any bugs, issues, or     #
# corrections to:                 #
# matt@summertech.net             #
#                                 #
#                                 #
# Module 5.1.2                    #
# - - - - - - - - - - - - - - - - #

#SUMMERTECH CONFIDENTIAL
#COPYRIGHT (C) 2017 SUMMERTECH, INC. ALL RIGHTS RESERVED

from Shape import Shape
from Point3D import Point3D

"""
Teaching Notes:

Goal: Have the student write their first derived class. Implement all
abstract methods. 

Remarks:
1. Most of the work has been done through Point3D and Shape. Note that 
we only define the methods we left empty in Shape, yet we are still able
to access getVertices and getNumVertices.
2. Assume the points are entered in the following order:

  A --- B
  |     |
  C --- D

Area is then a.distance(c) * c.distance(d)
Perimeter is the sum of each sides distance, or just
2 * a.distance(c) + 2 * a.distance(b)
"""

class Rectangle(Shape):
  
  def __init__(self, a, b, c, d):
    self.vertices = [a, b, c, d]
  
  def __str__(self):
    result = ""
    for i in self.vertices:
      result += str(i) + ","
    result = result[:-1]
    
    return "Rectangle: " + result

  def getArea(self):
    a = self.vertices[0]
    b = self.vertices[1]
    c = self.vertices[2]
    d = self.vertices[3]

    sideA = a.distance(c)
    sideB = c.distance(d)

    return sideA * sideB

  def getPerimeter(self):
    a = self.vertices[0]
    b = self.vertices[1]
    c = self.vertices[2]
    d = self.vertices[3]
    
    sideA = a.distance(c)
    sideB = a.distance(b)

    return 2*sideA + 2*sideB

a = Point3D(0, 1, 0)
b = Point3D(1, 1, 0)
c = Point3D(0, 0, 0)
d = Point3D(1, 0, 0)

rectangle = Rectangle(a, b, c, d)

print(rectangle)
print(rectangle.getVertices())
print(rectangle.getNumVertices())
print(rectangle.getArea()) #should be 1
print(rectangle.getPerimeter()) #should be 4
