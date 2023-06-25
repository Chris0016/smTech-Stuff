# - - - - - - - - - - - - - - - - #
# SummerTech/Coditum Curriculum   #
# Created by Matthew Baptist      #
#                                 #
# Report any bugs, issues, or     #
# corrections to:                 #
# matt@summertech.net             #
#                                 #
#                                 #
# Module 7.1.3                    #
# - - - - - - - - - - - - - - - - #

#SUMMERTECH CONFIDENTIAL
#COPYRIGHT (C) 2017 SUMMERTECH, INC. ALL RIGHTS RESERVED

"""
Teaching Notes
  
Goal: Implement the Graph Data Structure with Adjacency Lists. Apply reasoning to determine which implementation is appropriate for a given problem.

Remarks:

1. Efficiency Notes:
- O(2*E + N) Memory where E is the number of edges, and N is the number of Nodes.
- Iterating over all neighbors is fast, O( Neighbors ) as opposed to O(N)
- Checking for a connection is relatively slow O( Neighbors ) compared to O(1)
- Iterating over all edges is fast O(E) compared to O(n^2)
- Adding, modifying, or removing an edge is relatively slow O( Neighbors) compare to O(1)
- Starting up, O(N), and adding a new node, O(1), are cheap

2. For our purposes, the benefits in memory size and iteration over edges are going to be more significant than the penalty for lookup and modifying connections.

"""

class AdjacencyListGraph:

  def __init__(self, size):
    
    self.matrix = []
    
    for i in range(size):
      self.matrix.append([])
  
  #add, modify, or remove an edge
  def addEdge(self, source, dest, cost):
    self.matrix[source].append( (dest, cost) )
    self.matrix[dest].append( (source, cost) )

  def addNode(self):
    self.matrix.append([])

  def isConnected(self, source, dest):
    for i in range(len(self.matrix[source])):
      if (self.matrix[source][i][0] == dest):
        return True
    
    return False

  def getCost(self, source, dest):
    for i in range(len(self.matrix[source])):
      if (self.matrix[source][i][0] == dest):
        return self.matrix[source][i][1]

  def getNeighbors(self, source):
    neighbors = []
    for i in range(len(self.matrix[source])):
        neighbors.append(self.matrix[source][i][0])
    return neighbors

  #For testing purposes
  def printMatrix(self):
    for i in range(len(self.matrix)):
      for j in range(len(self.matrix[i])):
        print(repr(self.matrix[i][j]).ljust(9), end = "")
      print()

def main():

  cities = AdjacencyListGraph(8)
  cities.addEdge(0, 1, 10)
  cities.addEdge(0, 2, 5)
  cities.addEdge(2, 3, 15)
  cities.addEdge(1, 3, 7)
  cities.addEdge(3, 5, 6)
  cities.addEdge(3, 4, 2)
  cities.addEdge(4, 5, 3)
  cities.addEdge(4, 6, 2)
  cities.addEdge(4, 7, 5)
  cities.addEdge(5, 6, 3)
  cities.printMatrix()

if (__name__ == "__main__"):
  main()

"""
Extension:

1. Create a new class, AdjacencyListDiGraph that supports directed graphs. addEdge is the obvious method to modify, but does anything else need to be modified? (In the sample implementation, no, but there are potential dangers in getNeighbors, getCost, and isConnected depending on the student's implementation)

i.e. 
def addEdge(self, source, dest, cost):
  self.matrix[source].append( (dest, cost) )

2. Write a method, removeSelfLoops(), that returns a copy of the graph with any and all self loops removed. Caution: Be sure that you "deep copy" the graph so that the resulting graph does not share an array with the original graph.

def removeSelfLoops(self):
  temp = AdjacencyMatrixGraph(len(self.matrix))
  for i in range(len(self.matrix)):
    for j in range(len(self.matrix[i])):
      if (not i == self.matrix[i][j][0]):
        temp.matrix[i][j] = self.matrix[i][j]

"""
