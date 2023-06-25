# - - - - - - - - - - - - - - - - #
# SummerTech/Coditum Curriculum   #
# Created by Matthew Baptist      #
#                                 #
# Report any bugs, issues, or     #
# corrections to:                 #
# matt@summertech.net             #
#                                 #
#                                 #
# Module 6.0.3                    #
# - - - - - - - - - - - - - - - - #

#SUMMERTECH CONFIDENTIAL
#COPYRIGHT (C) 2017 SUMMERTECH, INC. ALL RIGHTS RESERVED

"""
Teacher Notes:

Goal: Reinforce the understanding of Linked Lists by using them to create another useful data structure. Introduce the Stack data structure.

Remarks:
1. Stack does not have to import and work with any Node objects, in fact it doesn't have to know anything about the internals of the linked list at all. It only has to know the linked list's public interface and performance guarantees.
2. The Stack simplifies adding and removing to the list by only adding or removing from the front of the linked list. Notice that its public interface (push/pop) requires fewer arguments (0-1 instead of 1-2). This is a further abstraction for the user.
3. Note: The stack does not add any significant functionality to what the linked list could already do. Instead, it allows us to describe a subset of that functionality in a more clear and less error prone way.
4. Since a Linked List has O(1) insertion and removal for a known location, both push and pop are O(1). Perhaps walk through this, visually and verbally, what's going on.
5. A lot of problems in computer science and in the every day world are naturally modeled with stacks (First In First Out)! An installation or task that has multiple dependencies? A course in school that has prerequsites? The way you eat a stack of pancakes? :D
6. Have we been working with Stacks all along? (the basic python list can be used as a stack [append/pop])
"""

from LinkedList import LinkedList

class Stack:

  def __init__(self):
    self.ll = LinkedList()

  def push(self, x):
    self.ll.add(x, 0)

  def pop(self):
    temp = self.ll.get(0)
    self.ll.delete(0)
    return temp

  def length(self):
    return self.ll.length()
