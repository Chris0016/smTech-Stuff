# - - - - - - - - - - - - - - - - #
# SummerTech/Coditum Curriculum   #
# Created by Matthew Baptist      #
#                                 #
# Report any bugs, issues, or     #
# corrections to:                 #
# matt@summertech.net             #
#                                 #
#                                 #
# Module 6.1.3                    #
# - - - - - - - - - - - - - - - - #

#SUMMERTECH CONFIDENTIAL
#COPYRIGHT (C) 2017 SUMMERTECH, INC. ALL RIGHTS RESERVED

"""
Teaching Notes
  
Goal: Apply Binary Search Trees in a meaningful context. Get a first look at working with associative containers (dictionaries).

Remarks:

1. A dictionary let's us store key-value pairs and look up values based on keys.
- The binary search tree that we implemented before does not provide a get method, since that wouldn't have made much sense in its original design. To add this, the student can edit the binary search tree itself or inherit from it to create a new class. The second is chosen in the implementation

2. Since the Dictionary has to store key with values, we create a Pair type to hold both the key and value. 
- Just like built-in methods such as __init__ and __str__, Python has built in methods __eq__, __lt__, __le__, __gt__, __ge__, and __ne__ that it knows to call to test ==, <, <=, >, >= and != respectively.
- Since our dictionary will be searching based on key, we define the comparisons based on the stored keys.

3. Rmk: After doing all the work to build the Binary Search Tree and the Pair objects, the dictionary itself is really simple.

4. Python has a built-in dictionary that we can use. In general, we should use Python's dictionary, this is just an example to show how one could possibly be implemented. Python dictionaries are actually implemented using a Hash Table, which we will learn about later.

"""

from BinarySearchTree import BinarySearchTree

class DictionaryTree(BinarySearchTree):
  def __init__(self):
    super().__init__()

  def get(self, x):
    return self._get(self.root, x)

  def _get(self, node, x):
    if (node == None):
      return None
    elif (node.getData() == x):
      return node.getData()
    elif (node.getData() < x):
      return self._get(node.getRight(), x)
    else:
      return self._get(node.getLeft(), x)

class Pair:
  def __init__(self, key, value):
    self.key = key
    self.value = value
        
  def __eq__(self, rhs):
    return self.key == rhs.key

  def __lt__(self, rhs):
    return self.key < rhs.key
  
  def __le__(self, rhs):
    return self.key <= rhs.key

  def __gt__(self, rhs):
    return self.key > rhs.key

class Dictionary:
  def __init__(self):
    self.tree = DictionaryTree()

  def add(self, key, value):
    temp = Pair(key, value)
    
    if self.tree.contains(temp):
      self.tree.remove(temp)
    
    self.tree.add(Pair(key, value))

  def get(self, key):
    temp = Pair(key, None)
    return self.tree.get(temp).value

d = Dictionary()

d.add("John", 10)
d.add("Jane", 15)
d.add("Adam", 0)
d.add("Zoe", 30)

print(d.get("John"))
print(d.get("Jane"))
print(d.get("Adam"))
print(d.get("Zoe"))


