# - - - - - - - - - - - - - - - - #
# SummerTech/Coditum Curriculum   #
# Created by Matthew Baptist      #
#                                 #
# Report any bugs, issues, or     #
# corrections to:                 #
# matt@summertech.net             #
#                                 #
#                                 #
# Module 6.0.2                    #
# - - - - - - - - - - - - - - - - #

#SUMMERTECH CONFIDENTIAL
#COPYRIGHT (C) 2017 SUMMERTECH, INC. ALL RIGHTS RESERVED

"""
Teaching Notes

Goal: Introduce the motivation behind studying Data Structures. Learn about the linked list data structure.

"""

class LinkedList:
  def __init__(self):
    self.size = 0
    self.head = None
  
  def add(self, val, pos):
    temp = Node(val)
    self.addNode(temp, pos)
  
  def delete(self, pos):
    self.deleteNode(pos)
  
  def get(self, pos):
    temp = self.head

    for i in range(pos):
      if (temp == None):
        assert(not temp == None)
      else:
        temp = temp.getLink()
    return temp.data

  def addNode(self, node, pos):
    assert(pos <= self.size) #Can't insert into a position that doesn't exist
    self.size += 1
    ptr = self.head
    
    if (pos == 0):
      node.addLink(self.head)
      self.head = node
    else:
      for i in range(pos - 1):
        ptr = ptr.getLink()
      node.addLink(ptr.getLink())
      ptr.addLink(node)

  def deleteNode(self, pos):
    assert(pos < self.size and pos >= 0)
    self.size -= 1
  
    if (pos == 0):
      self.head = self.head.getLink()
    else:
      ptr = self.head
      for i in range(pos-1):
        ptr = ptr.getLink()
      ptr.addLink(ptr.getLink().getLink())

  def printList(self):
    ptr = self.head
    
    while (ptr != None):
      print(str(ptr), end=" ")
      ptr = ptr.getLink()
    print()

  def length(self):
    return self.size
