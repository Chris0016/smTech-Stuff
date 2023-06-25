# - - - - - - - - - - - - - - - - #
# SummerTech/Coditum Curriculum   #
# Created by Matthew Baptist      #
#                                 #
# Report any bugs, issues, or     #
# corrections to:                 #
# matt@summertech.net             #
#                                 #
#                                 #
# Module 7.1.1                    #
# - - - - - - - - - - - - - - - - #

#SUMMERTECH CONFIDENTIAL
#COPYRIGHT (C) 2017 SUMMERTECH, INC. ALL RIGHTS RESERVED

"""
Teaching Notes
  
Goal: Introduce and implement the Graph Data Structure. Learn about problems that are naturally represented by Graphs.

Remarks:

1. Graphs have immediate real world applications, connect this to practical things that students are familiar with. i.e. Uber and Google Maps, movie or item recommendations from Netflix or Amazon, suggested Friends/Pages on Facebook, decisions made by an AI.

2. Draw out a graph on a whiteboard or pencil and paper for the student. Connect it to a real world topic, perhaps a social graph of people and their friends or a simple graph that represents cities and the costs to travel between them.

3. There are many types of graphs and even more ways to implement them. We will cover two common and useful ones, Adjacency Matrices and Adjacency Lists for undirected weighted graphs. We will compare the relative strengths and weaknesses of both approaches after learning about both.
- The approach used can easily be extended to provide directed graphs. If the student is advanced and interested, consider asking them how they would go about modifying this program to make the graph directed. This is provided as an extension below.

4. Adjacency Matrices uses O(n^2) memory, where n is the number of nodes in the graph. Have the student think about why this may not be desirable. What happens when there are millions of nodes, like a real world navigation system or social network?

5. Conventions: 
- A connection from node i to node j with weight c is stored at self.matrix[i][j] //Holds c
- No connection between node i and j is represented as a -1 at matrix[i][j] (Can the student say why we might choose -1 over 0? How could we handle it if we wanted our graph to hold negative weights or unweighted integers?)
- Since the graph is undirected, the matrix is symmetric, that is if matrix[i][j] = c, then matrix[j][i] = c as well.

6. Other notes for after the graph is implemented:
- Checking for an edge between i and j is very cheap O(1)
- Getting a list of connected nodes for an y is relatively expensive O(n), this also suggests that iterating over all edges is expensive.
- Adding a new node is expensive O(n)
- Adding new edges, modifying existing edges, removing edges are all cheap tho.


7. Draw some sample graphs, recreate with the AdjacencyMatrixGraph and print out the contents of the self.matrix 2D Array. Look at the values for a sparse graph (few connections) vs a full graph (many connections). We can visually see some of the strengths and weaknesses of the Adjacency Matrix.

"""

class AdjacencyMatrixGraph:

  def __init__(self, size):
    
    self.matrix = []
    
    for i in range(size):
      self.matrix.append([])
      for j in range(size):
        self.matrix[i].append(-1)

  #add, modify, or remove an edge
  def addEdge(self, source, dest, cost):
    self.matrix[source][dest] = cost
    self.matrix[dest][source] = cost

  def addNode(self):
    self.matrix.append([])
    
    #Add the new row
    for i in range(len(self.matrix)):
      self.matrix[len(self.matrix) - 1].append(-1)
    
    #Add an additional column to each other row
    for i in range(len(self.matrix) - 1):
      self.matrix[i].append(-1)

  def isConnected(self, source, dest):
    if (self.matrix[source][dest] == -1):
      return False
    else:
      return True

  def getCost(self, source, dest):
    return self.matrix[source][dest]

  def getNeighbors(self, source):
    neighbors = []
    for i in range(len(self.matrix)):
      if (not self.matrix[source][i] == -1):
        neighbors.append(i)

  #For testing purposes
  def printMatrix(self):
    for i in range(len(self.matrix)):
      for j in range(len(self.matrix)):
        print(repr(self.matrix[i][j]).rjust(3), end = "")
      print()

def main():

  cities = AdjacencyMatrixGraph(8)
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

1. Create a new class, AdjacencyMatrixDiGraph that supports directed graphs. addEdge is the obvious method to modify, but does anything else need to be modified? (In the sample implementation, no, but there are potential dangers in getNeighbors, getCost, and isConnected depending on the student's implementation)

i.e. 
def addEdge(self, source, dest, cost):
  self.matrix[source][dest] = cost

2. Write a method, removeSelfLoops(), that returns a copy of the graph with any and all self loops removed. Caution: Be sure that you "deep copy" the graph so that the resulting graph does not share an array with the original graph.

def removeSelfLoops(self):
  temp = AdjacencyMatrixGraph(len(self.matrix))
  for i in range(len(self.matrix)):
    for j in range(len(self.matrix)):
      if (not i == j):
        temp.matrix[i][j] = self.matrix[i][j]
      else:
        temp.matrix[i][j] = -1

- Can you think of an application where removing self loops might be important?

"""
