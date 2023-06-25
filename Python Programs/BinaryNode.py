# - - - - - - - - - - - - - - - - #
# SummerTech/Coditum Curriculum   #
# Created by Matthew Baptist      #
#                                 #
# Report any bugs, issues, or     #
# corrections to:                 #
# matt@summertech.net             #
#                                 #
#                                 #
# Module 6.1.1                    #
# - - - - - - - - - - - - - - - - #

#SUMMERTECH CONFIDENTIAL
#COPYRIGHT (C) 2017 SUMMERTECH, INC. ALL RIGHTS RESERVED

"""
Teaching Notes

Goal:
"""

class BinaryNode:

  def __init__(self, data):
    self.left = None
    self.right = None
    self.data = data

  def addLeft(self, left):
    self.left = left

  def addRight(self, right):
    self.right = right

  def getLeft(self):
    return self.left

  def getRight(self):
    return self.right

  def setData(self, data):
    self.data = data

  def getData(self):
    return self.data
