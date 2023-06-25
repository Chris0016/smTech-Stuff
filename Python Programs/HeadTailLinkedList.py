
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

class LinkedList:
  def __init__(self):
    self.size = 0
    self.head = None
    self.tail = None
  
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
    elif (pos == self.size - 2):
      self.tail.addLink(node)
      self.tail = self.tail.getLink()
    else:
      for i in range(pos - 1):
        ptr = ptr.getLink()
      node.addLink(ptr.getLink())
      ptr.addLink(node)

    if (self.size == 1):
      self.tail = self.head
    elif (not self.tail.getLink() == None):
      self.tail = self.tail.getLink()

  def deleteNode(self, pos):
    assert(pos < self.size and pos >= 0)
    self.size -= 1
  
    if (self.size == 0):
      self.tail = None
  
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
