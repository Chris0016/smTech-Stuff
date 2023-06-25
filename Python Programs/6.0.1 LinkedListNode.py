# - - - - - - - - - - - - - - - - #
# SummerTech/Coditum Curriculum   #
# Created by Matthew Baptist      #
#                                 #
# Report any bugs, issues, or     #
# corrections to:                 #
# matt@summertech.net             #
#                                 #
#                                 #
# Module 6.0.1                    #
# - - - - - - - - - - - - - - - - #

#SUMMERTECH CONFIDENTIAL
#COPYRIGHT (C) 2017 SUMMERTECH, INC. ALL RIGHTS RESERVED

"""
Teaching Notes

Goal: Introduce the motivation behind studying Data Structures. Learn about the linked list data structure.

Remarks:
Use Linked Lists as a vehicle for teaching the more fundamental ideas.
  
1. Algorithmic Analysis, Computational Complexity, Big-Oh Notation
- Up until now, we haven't seriously discussed the speed or efficiency of programs. However, this is clearly an area of importance. When faced with many approaches of doing something, how do we pick one? What should we balance- speed, clear and concise code, memory?
- Building the motivation behind Algorithmic Analysis with a simple series of questions is recommended. (The questions and answers here may seem verbose, but you can have this conversation in under 5 minutes) :
  i) How could we compare the speed between two programs? Let the student think about it and answer.
  - Timing is variable, a program may take more or less time to complete due to factors out of the programmers control such as the operating system, system events, or hardware. Two approaches might take different amounts of time depending on the input.
  - Counting processor cycles and then comparing between two programs reduces some of the variability in timing, but most probles remain.
  - There's an even more fundamental issue with both of these approaches. Deciding by timing or counting our programs requires us to actually try both solutions before we can compare them. If our project was large with multiple people contributing, it might take months to implement either solution. Making both just to compare them is a big waste of time and money! We need to be able to compare approaches without having to write both ahead of time.
  ii) How would we compare a program that has a high start up cost but then runs quickly afterwards vs a program that starts up quickly but then runs more slowly for every operation afterwards?
  - As the size of the input to the program grows, the second method is clearly superior. Why? Graph the scenario on the whiteboard for the student.
  - Modern inputs to programs are extremely large, so we almost always write our programs with the second case in mind. We will usually pass the cutoff point.
  iii) If we know roughly how different program behave as its input grows, we can compare them without having to know any exact timings or details. How?
  - Walk through graphing a constant function, a linear function, and a quadratic function with the student, and showing that they intersect for large enough input size (x). It doesn't matter what coefficients we put on the functions, we can always find an intersection point by choosing a larger x.
  iv) The way of describing this idea is with Big-Oh Notation. i.e. O(15n^2 + 8n + 2000) = O(n^2)
  
2. Data Structures
- Programmers study data structures to learn effective ways to store and work with data that efficiently solve problems.
- Data structures are building blocks of more complicated programs, not an end goal in and of themselves. i.e. Google Maps uses many data structures, graphs, stacks, hash maps, and more in order to quickly find routes for you, but Google Maps is more than the sum of its parts.
- Data Structures are an abstraction. There may be many different ways of implementing any one data structure, as long as each possible solution has the same time-complexity and consistency for the user of the data structure. 

3. Linked Lists
- A Linked List is a simple data structure
- Draw the nodes and links between them for a sample linked list
- Don't worry about the analysis of the Linked List yet.

"""

class Node:
  def __init__(self, data):
    self.data = data
    self.link = None

  def addLink(self, link):
    self.link = link
  
  def getLink(self):
    return self.link

  def __str__(self):
    return str(self.data)
