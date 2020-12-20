from doubly_linked_list import DoublyLinkedList

class Queue(DoublyLinkedList):
  def __init__(self):
    DoublyLinkedList.__init__(self)

  def is_empty(self):
    return self.length == 0
  
  def peek(self):
    return self.head.element
  
  def push(self, element):
    self.append(element)
  
  def pop(self):
    if self.length > 0:
      element = self.head.element
      self.remove(element)
      return element
    return None

# test code
queue = Queue()
queue.push(5)
queue.push(2)
queue.push(4)
queue.push(3)

print(queue)

print(queue.pop())
print(queue.pop())
print(queue.pop())
print(queue.pop())
print(queue.pop())