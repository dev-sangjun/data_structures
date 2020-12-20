from linked_list import IndexOutOfRangeError

class Node:
  def __init__(self, element = None):
    self.element = element
    self.prev = None
    self.next = None

  def __str__(self):
    return str(self.element)
  
class DoublyLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0

  def prepend(self, element):
    node = Node(element)
    # if the linked list was empty
    if self.head == None:
      self.head = node
      self.tail = node
    else:    
      node.next = self.head
      self.head.prev = node
      self.head = node
    self.length += 1

  def append(self, element):
    node = Node(element)
    # if the linked list was empty
    if self.head == None:
      self.head = node
      self.tail = node
    else:    
      node.prev = self.tail
      self.tail.next = node
      self.tail = node
    self.length += 1

  def get(self, index):
    if index >= self.length or index < 0:
      raise IndexOutOfRangeError()
    else:
      cur = self.head
      for _ in range(index):
        cur = cur.next
      return cur

  def find(self, element):
    cur = self.head
    index = 0
    while cur != None:
      if cur.element == element:
        return index
      cur = cur.next
      index += 1
    return -1

  def insert(self, element, index):
    if index > self.length or index < 0:
      raise IndexOutOfRangeError()
    elif index == 0:
      self.prepend(element)
    elif index == self.length:
      self.append(element)
    else:
      node = Node(element)
      cur = self.get(index)
      cur.prev.next = node
      node.prev = cur.prev
      node.next = cur
      cur.prev = node

  def remove(self, element):
    index = self.find(element)
    if index != -1:
      if self.length == 1:
        self.head = None
        self.tail = None
        self.length -= 1
        return
      cur = self.get(index)
      if cur == self.head:
        self.head = cur.next
        self.head.prev = None
      elif cur == self.tail:
        self.tail = cur.prev
        self.tail.next = None
      else:
        cur.prev.next = cur.next
        cur.next.prev = cur.prev
      self.length -= 1

  def __str__(self):
    elements = []
    cur = self.head
    while cur != None:
      elements.append(cur.element)
      cur = cur.next
    return str(elements)

# test code
doubly_linked_list = DoublyLinkedList()