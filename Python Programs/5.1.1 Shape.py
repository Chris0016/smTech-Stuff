# - - - - - - - - - - - - - - - - #
# SummerTech/Coditum Curriculum   #
# Created by Matthew Baptist      #
#                                 #
# Report any bugs, issues, or     #
# corrections to:                 #
# matt@summertech.net             #
#                                 #
#                                 #
# Module 5.1.1                    #
# - - - - - - - - - - - - - - - - #

#SUMMERTECH CONFIDENTIAL
#COPYRIGHT (C) 2017 SUMMERTECH, INC. ALL RIGHTS RESERVED

"""
Teaching Notes:

Goal: Introduce the concepts of Inheritance, Interfaces, and Polymorphism.

Remarks:
1. Shape is an abstract base class, notice the behaviors that we define for all derived
classes, (__str__, getArea, getPerimeter), but provide no implementation for. 
2. However, some behaviors, getVertices and getNumVertices are defined in the abstract class.
3. These methods provide a common interface for us to work with shapes of any derived type.

"""

class Shape:
  def __str__(self):
    pass
  def getVertices(self):
    return self.vertices
  def getNumVertices(self):
    return len(self.vertices)
  def getArea(self):
    pass
  def getPerimeter(self):
    pass
