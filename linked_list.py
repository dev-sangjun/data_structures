class IndexOutOfRangeError(Exception):
  def __init__(self, message):
    self.message = message
  def __str__(self):
    return self.message

class Node:
  def __init__(self, element = None):
    self.element = element
    self.next = None
  
  def __str__(self):
    return str(self.element)

class LinkedList:
  def __init__(self):
    self.head = None
    self.length = 0

  def append(self, element):
    node = Node(element)
    if self.head == None:
      # the list is empty
      self.head = node
    else:
      cur = self.head
      while cur.next != None:
        cur = cur.next
      cur.next = node
    self.length += 1

  def get(self, index):
    if index >= self.length or index < 0:
      raise IndexOutOfRangeError("Index is out of range")
    else:
      cur = self.head
      for _ in range(index):
        cur = cur.next
      return cur.element

  def remove(self, index):
    if index >= self.length or index < 0:
      raise IndexOutOfRangeError("Index is out of range")
    else:
      cur = self.head
      if index == 0:
        self.head = cur.next
      else:
        prev_node = None
        for _ in range(index):
          prev_node = cur
          cur = cur.next
        prev_node.next = cur.next

  def __str__(self):
    elements = []
    cur = self.head
    while cur != None:
      elements.append(cur.element)
      cur = cur.next
    return str(elements)

# test code
linked_list = LinkedList()