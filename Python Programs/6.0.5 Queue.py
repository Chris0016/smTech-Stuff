# - - - - - - - - - - - - - - - - #
# SummerTech/Coditum Curriculum   #
# Created by Matthew Baptist      #
#                                 #
# Report any bugs, issues, or     #
# corrections to:                 #
# matt@summertech.net             #
#                                 #
#                                 #
# Module 6.0.5                    #
# - - - - - - - - - - - - - - - - #

#SUMMERTECH CONFIDENTIAL
#COPYRIGHT (C) 2017 SUMMERTECH, INC. ALL RIGHTS RESERVED

"""
Teacher Notes

Goal: Learn about the Queue data structure and problems with an inherent FIFO structure.

Remarks:
1. There are several valid ways to approach this. Modifying the Linked List from 6.0.2 so that it stores a reference to its final node as well as the head (called a Head-Tail Linked List) is recommended. Alternatively, a queue can be made from two stacks (Given as an extension below).

"""

from HeadTailLinkedList import LinkedList

class Queue:

  def __init__(self):
    self.ll = LinkedList()

  def enqueue(self, x):
    self.ll.add(x, self.length())

  def dequeue(self):
    temp = self.ll.get(0)
    self.ll.delete(0)
    return temp

  def length(self):
    return self.ll.length()

q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(q.dequeue())
print(q.dequeue())
print(q.dequeue())

q.enqueue(4)
q.enqueue(5)
q.enqueue(6)

print(q.dequeue())
print(q.dequeue())
print(q.dequeue())

q.enqueue(7)
print(q.dequeue())
q.enqueue(8)
print(q.dequeue())
q.enqueue(9)
print(q.dequeue())


"""
Extension:
1. Implement the queue using two stacks instead of modifying the 6.0.2 Linked List into a Head-Tail Linked List.
"""
