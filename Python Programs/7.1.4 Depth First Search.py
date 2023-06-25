# - - - - - - - - - - - - - - - - #
# SummerTech/Coditum Curriculum   #
# Created by Matthew Baptist      #
#                                 #
# Report any bugs, issues, or     #
# corrections to:                 #
# matt@summertech.net             #
#                                 #
#                                 #
# Module 7.1.4                    #
# - - - - - - - - - - - - - - - - #

#SUMMERTECH CONFIDENTIAL
#COPYRIGHT (C) 2017 SUMMERTECH, INC. ALL RIGHTS RESERVED

"""
Teaching Notes
  
Goal: Introduce search problems. Learn and implement the DFS Algorithm. Identify situations where DFS is appropriate.

Remarks:

"""

from AdjacencyListGraph import AdjacencyListGraph
from collections import deque

def breadthfirstsearch(graph, source):
  explored = {}
  reachable = []
  queue = deque()

  reachable.append(source)
  explored[source] = True
  
  for neighbor in graph.getNeighbors(source):
    queue.append(neighbor)

  while (len(queue) > 0):
    node = queue.popleft()

    reachable.append(node)
    explored[node] = True

    for neighbor in graph.getNeighbors(node):
      if neighbor not in explored:
        queue.append(neighbor)

  return reachable


def depthfirstsearch(graph, source):
  explored = {}
  reachable = []

  reachable.append(source)
  explored[source] = True

  return _depthfirstsearch(graph, source, explored, reachable)

def _depthfirstsearch(graph, source, explored, reachable):
  
  for neighbor in graph.getNeighbors(source):
    if not neighbor in explored:
      reachable.append(neighbor)
      explored[neighbor] = True
      _depthfirstsearch(graph, neighbor, explored, reachable)

  return reachable

def main():

  graph = AdjacencyListGraph(8)

  graph.addEdge(0, 1, 1)
  graph.addEdge(0, 4, 1)
  graph.addEdge(0, 5, 1)
  graph.addEdge(1, 2, 1)
  graph.addEdge(1, 3, 1)
  graph.addEdge(5, 6, 1)

  ordering = depthfirstsearch(graph, 0)
  print(ordering)

  ordering2 = breadthfirstsearch(graph, 0)
  print(ordering2)

if (__name__ == "__main__"):
  main()
