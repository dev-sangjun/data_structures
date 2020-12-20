from doubly_linked_list import DoublyLinkedList

class Stack(DoublyLinkedList):
  def __init__(self):
    DoublyLinkedList.__init__(self)

  def is_empty(self):
    return self.length == 0
  
  def peek(self):
    return self.head.element
  
  def push(self, element):
    self.prepend(element)
  
  def pop(self):
    if self.length > 0:
      element = self.head.element
      self.remove(element)
      return element
    return None

  

stack = Stack()
stack.push(5)
stack.push(2)
stack.push(4)
stack.push(3)

print(stack)

print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())