# - - - - - - - - - - - - - - - - #
# SummerTech/Coditum Curriculum   #
# Created by Matthew Baptist      #
#                                 #
# Report any bugs, issues, or     #
# corrections to:                 #
# matt@summertech.net             #
#                                 #
#                                 #
# Module 6.1.4                    #
# - - - - - - - - - - - - - - - - #

#SUMMERTECH CONFIDENTIAL
#COPYRIGHT (C) 2017 SUMMERTECH, INC. ALL RIGHTS RESERVED

"""
Teaching Notes
  
Goal: Learn about, analyze, and implement an AVL Tree.

Remarks:

1. Start by demonstrating what can go wrong with a binary search tree, i.e. a bad sequence of input leading to an unbalanced tree. What is the time complexity in this situation? An AVL Tree, then, is understood as a way to enforce tree balance and maintain fast lookups.
- On a whiteboard or piece of paper, simulate a sequence of inputs and calculate the balancefactors, perform left, right, left-right, and right-left rotations as necessary in order to show the student how it works.
- Identify the 4 cases and the rules for each.

2. It's simplest to start by copying and pasting the binary search tree. Ask the student what needs to be modified from the original tree. (insert and remove)
- It is recommended to start with insert before attempting remove.

3. There is a nice graphic for students to visualize tree rotations on wikipedia at the below link. However, encourage students not to view the sample code implementation provided below. 
- https://en.wikipedia.org/wiki/AVL_tree#/media/File:AVL_Tree_Example.gif

"""

from BinaryNode import BinaryNode
from random import randint

class AVLNode(BinaryNode):

  def __init__(self, x):
    super().__init__(x)
    self.maxheight = 0
    self.balancefactor = 0

  def update(self):
    lheight = -1
    rheight = -1
    
    if (self.left):
      lheight = self.left.maxheight
    if (self.right):
      rheight = self.right.maxheight

    self.maxheight = max(lheight + 1, rheight + 1)
    self.balancefactor = rheight - lheight

class AVLTree:

  def __init__(self):
    self.root = None
    self.size = 0

  def add(self, x):
    self.size += 1
    self.root = self._add(self.root, x)
  
  def _add(self, node, x):
    if (node == None):
      node = AVLNode(x)
    elif (x <= node.getData()):
      node.left = self._add(node.getLeft(), x)
    else:
      node.right = self._add(node.getRight(), x)

    node.update()
    return self.balance(node)
      
  def balance(self, node):
   #Right-heavy: Left Rotation or Right + Left Rotation
    if (node.balancefactor > 1):
      if (node.right and node.right.balancefactor > 0):
        node = self.leftrotation(node)
      elif (node.right and node.right.balancefactor == -1):
        node.right = self.rightrotation(node.right)
        node = self.leftrotation(node)
    #Left-heavy: Right Rotation or Left + Right Rotation
    elif (node.balancefactor < -1):
      if (node.left and node.left.balancefactor == -1):
        node = self.rightrotation(node)
      elif (node.left and node.left.balancefactor == 1):
        node.left = self.leftrotation(node.left)
        node = self.rightrotation(node)

    #update heights and weights?

    return node
        
  def rightrotation(self, node):
    #Rotate the node's left root into the node
    rsubtree = node.left.right
    node.left.right = node
    node = node.left
    node.right.left = rsubtree
    
    node.right.update()
    node.update()
  
    return node

  def leftrotation(self, node):
    #Rotate the node's left root into the node
    lsubtree = node.right.left
    node.right.left = node
    node = node.right
    node.left.right = lsubtree
    
    node.left.update()
    node.update()
    
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
  tree = AVLTree()

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

  tree = AVLTree()
  for i in range(15):
    tree.add(randint(0, 1000))
  tree.sidewaysPrint()

if (__name__ == "__main__"):
  main()
