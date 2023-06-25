
# - - - - - - - - - - - - - - - - #
# SummerTech/Coditum Curriculum   #
# Created by Matthew Baptist      #
#                                 #
# Report any bugs, issues, or     #
# corrections to:                 #
# matt@summertech.net             #
#                                 #
#                                 #
# Module 5.1.5                    #
# - - - - - - - - - - - - - - - - #

#SUMMERTECH CONFIDENTIAL
#COPYRIGHT (C) 2017 SUMMERTECH, INC. ALL RIGHTS RESERVED

"""
Teaching Notes:

Goal: Putting it all together. Iterate over a list of derived Shape objects, 
talking to each through the shared interface.

Remarks:

1. The final for loop makes no reference to the type of Shape stored in the mesh list.
This is Polymorphism, all the derived classes share an interface and can be accessed the
same way. 

2. While our "mesh" has no real use in computer graphics, a real mesh is very similar
to our final list of vertices generated in the end. A mesh is the collection of vertices, 
edges, and faces that make up a 3D model. It's not a far jump from out program to generating 
an actual list of vertices and edges for a 3D representation.
  
"""

from Shape import Shape
from Point3D import Point3D
from Rectangle import Rectangle
from Triangle import Triangle
from Trapezoid import Trapezoid

#Triangle
a = Point3D(0,2,0)
b = Point3D(0,0,0)
c = Point3D(2,0,0)
triangle = Triangle(a, b, c) #area: 2

#Rectangle
d = Point3D(0,2,0)
e = Point3D(2,2,0)
f = Point3D(0,0,0)
g = Point3D(2,0,0)
rectangle = Rectangle(d, e, f, g) #area: 4

#Trapezoid
h = Point3D(4,3,0)
i = Point3D(10,3,0)
j = Point3D(0,0,0)
k = Point3D(10,0,0)
trapezoid = Trapezoid(h, i, j, k) #area: 24

vertices = []

mesh = [triangle, rectangle, trapezoid]

for shape in mesh:
  print(shape)
  print("Area", shape.getArea())
  print("Perimeter", shape.getPerimeter())
  print()

  for vertex in shape.getVertices():
    vertices.append(vertex)

print("Vertex list")
for vertex in vertices:
  print(vertex)

"""
Super Challenge: Read about Face-Vertex Meshes, extend the Shape and Mesh programs
to generate face-vertex meshes. (Focus on Shape, Triangle, and Mesh first, then Rectangle)
  
"""
