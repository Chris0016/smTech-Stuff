# - - - - - - - - - - - - - - - - #
# SummerTech/Coditum Curriculum   #
# Created by Matthew Baptist      #
#                                 #
# Report any bugs, issues, or     #
# corrections to:                 #
# matt@summertech.net             #
#                                 #
#                                 #
# Module 6.1.2                    #
# - - - - - - - - - - - - - - - - #

#SUMMERTECH CONFIDENTIAL
#COPYRIGHT (C) 2017 SUMMERTECH, INC. ALL RIGHTS RESERVED

"""
Teaching Notes
  
Goal: Fully implement and test a Binary Search Tree.

"""

from BinaryNode import BinaryNode

class BinarySearchTree:

  def __init__(self):
    self.root = None
    self.size = 0

  def add(self, x):
    self.size += 1
    self.root = self._add(self.root, x)
  
  def _add(self, node, x):
    if (node == None):
      node = BinaryNode(x)
    elif (x <= node.getData()):
      node.left = self._add(node.getLeft(), x)
    else:
      node.right = self._add(node.getRight(), x)

    return node
  
  def printTree(self):
    self._printTree(self.root)

  def _printTree(self, node):
    if (not node == None):
      self._printTree(node.getLeft())
      print(node.getData())
      self._printTree(node.getRight())

  def sidewaysPrint(self):
    self._sidewaysPrint(self.root, 0)
  
  def _sidewaysPrint(self, node, depth):
    if (not node == None):
      self._sidewaysPrint(node.getRight(), depth + 1)
      print("  " * depth + str(node.getData()))
      self._sidewaysPrint(node.getLeft(), depth + 1)
  
  def remove(self, x):
    self.size -= 1
    self.root = self._remove(self.root, x)

  def _remove(self, node, x):
    if (node == None):
      return None
    elif (node.getData() == x):
      #Case 1 - Leaf
      if (node.getLeft() == None and node.getRight() == None):
        return None
      #Case 3 - Two children
      elif (node.getLeft() and node.getRight()):
        successor = self.inorderSuccessor(node.getRight())
        node.setData(successor.getData())
        successor.setData(x)
        node.addRight(self._remove(node.getRight(), x))
        return node
      #Case 2 - One Child
      else:
        if (node.getLeft() == None):
          return node.getRight()
        else:
          return node.getLeft()
    elif (node.getData() > x):
      node.addLeft(self._remove(node.getLeft(), x))
      return node
    else:
      node.addRight(self._remove(node.getRight(), x))
      return node

  def inorderSuccessor(self, node):
    if (not node.getLeft() == None):
      return self.inorderSuccessor(node.getLeft())
    else:
      return node

  def contains(self, x):
    return self._contains(self.root, x)
  
  def _contains(self, node, x):
    if (node == None):
      return False
    elif (node.getData() == x):
      return True
    elif (node.getData() < x):
      return self._contains(node.getRight(), x)
    else:
      return self._contains(node.getLeft(), x)

  def length(self):
    return self.size

def main():
  tree = BinarySearchTree()

  tree.add(10)
  tree.add(5)
  tree.add(3)
  tree.add(7)
  tree.add(15)
  tree.add(12)
  tree.add(17)
  tree.add(1)
  tree.add(4)
  tree.add(25)
  tree.add(30)

  tree.printTree()
  tree.sidewaysPrint()

  #Should be True
  print("Expected true:", tree.contains(10))
  print("Expected true:", tree.contains(1))
  print("Expected true:", tree.contains(4))
  print("Expected true:", tree.contains(30))
  print("Expected true:", tree.contains(12))

  #Should be False
  print("Expected false:", tree.contains(26))
  print("Expected false:", tree.contains(0))
  print("Expected false:", tree.contains(8))
  print("Expected false:", tree.contains(11))

  tree.remove(25)
  tree.sidewaysPrint()
  tree.remove(4)
  tree.sidewaysPrint()
  tree.remove(15)
  tree.sidewaysPrint()

if (__name__ == "__main__"):
  main()
