# - - - - - - - - - - - - - - - - #
# SummerTech/Coditum Curriculum   #
# Created by Matthew Baptist      #
#                                 #
# Report any bugs, issues, or     #
# corrections to:                 #
# matt@summertech.net             #
#                                 #
#                                 #
# Module 5.1.4                    #
# - - - - - - - - - - - - - - - - #

#SUMMERTECH CONFIDENTIAL
#COPYRIGHT (C) 2017 SUMMERTECH, INC. ALL RIGHTS RESERVED

from Shape import Shape
from Point3D import Point3D

"""
Teaching Notes:

Goal: Reinforce the concept of derived classes. Implement all abstract methods.

Remarks:

1. Most of the work has been done through Point3D and Shape. Note that
we only define the methods we left empty in Shape, yet we are still able
to access getVertices and getNumVertices.

2. Assume the points are entered in the following order:

 A---B
/    |
C----D


Perimeter is the sum of each sides distance
a.distance(c) + a.distance(b) + b.distance(d) + c.distance(d)

We'll assume that B-D gives the height, otherwise we would have to solve 
a system of equations, use trig, use projections, etc.

Area is then (c.distance(d) + a.distance(b))/2 * b.distance(d)
"""

class Trapezoid(Shape):
  
  def __init__(self, a, b, c, d):
    self.vertices = [a, b, c, d]
  
  def __str__(self):
    result = ""
    for i in self.vertices:
      result += str(i) + ","
    result = result[:-1]
    
    return "Trapezoid: " + result
  
  def getArea(self):
    
    a = self.vertices[0]
    b = self.vertices[1]
    c = self.vertices[2]
    d = self.vertices[3]
    
    sideA = a.distance(b)
    sideB = c.distance(d)
    height = b.distance(d)
    
    return (sideA + sideB) / 2 * height
  
  
  def getPerimeter(self):
    a = self.vertices[0]
    b = self.vertices[1]
    c = self.vertices[2]
    d = self.vertices[3]
    
    sideA = a.distance(c)
    sideB = a.distance(b)
    sideC = c.distance(d)
    sideD = b.distance(d)
    
    return sideA + sideB + sideC + sideD


a = Point3D(2, 1, 0)
b = Point3D(4, 1, 0)
c = Point3D(0, 0, 0)
d = Point3D(4, 0, 0)

trapezoid = Trapezoid(a, b, c, d)

print(trapezoid)
print(trapezoid.getVertices())
print(trapezoid.getNumVertices())
print(trapezoid.getArea()) #should be 3
print(trapezoid.getPerimeter()) #should be ~9.2361

"""
Challenge: Use projection to find the height and area of a general trapezoid. 
           (Appropriate for older students with a knowledge of math and with 
           an interest in computer graphics or application.)

#Point3D objects are a standin for vectors here
CD = Point3D(d.x - c.x, d.y - c.y, d.z - c.z)
CB = Point3D(b.x - c.x, b.y - c.y, b.z - c.z)

#Calculate the dot product and the magnitude of the projection axis to calculate the projection
dot = CD.x * CB.x + CD.y * CB.y + CD.z * CB.z
CD_MAG = CD.x * CD.x + CD.y * CD.y + CD.z * CD.z

CB.x = CB.x - dot * CD.x / CD_MAG #Original x term - Projected x term
CB.y = CB.y - dot * CD.y / CD_MAG #Original y term - Projected y term
CB.z = CB.z - dot * CD.z / CD_MAG #Original z term - Projected z term

origin = Point3D(0, 0, 0)
height = origin.distance(CB)

area = height * 1/2 * (c.distance(d) + a.distance(b))

#Using the following points: 
a = Point3D(3, 4, 0)
b = Point3D(13, 4, 0)
c = Point3D(0, 0, 0)
d = Point3D(16, 0, 0)

You should get area = 52, perimeter = 36

"""
