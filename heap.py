'''
array method:
  parent: (index - 2) / 2
  left: index * 2 + 1
  right: index * 2 + 2
'''

class Heap:
  def __init__(self):
    self.root = None
    self.list = []
  
  def insert(self, element):
    if not self.list:
      self.list.append(element)
      return
    else:
      index = len(self.list)
      self.list.append(element)
      self.move_up(index)
  
  def pop(self):
    if not self.list:
      return None
    else:
      last_index = len(self.list) - 1
      self.list[0], self.list[last_index] = self.list[last_index], self.list[0]
      self.list.pop(last_index)
      self.move_down(0)

  def move_up(self, index):
    if index < 1:
      return
    else:
      parent = self.get_parent(index)
      if self.list[index] < self.list[parent]:
        self.list[index], self.list[parent] = self.list[parent], self.list[index]
        self.move_up(parent)

  def move_down(self, index):
    if index >= len(self.list):
      return
    else:
      left_index = self.get_left(index)
      right_index = self.get_right(index)
      if left_index != -1:
        # compare the two childs
        smaller_index = left_index
        if right_index != -1:
          smaller_index = right_index if self.list[right_index] < self.list[left_index] else left_index
        self.list[index], self.list[smaller_index] = self.list[smaller_index], self.list[index]
        self.move_down(smaller_index)


  def get_parent(self, index):
    return (index - 1) // 2
  
  def get_left(self, index):
    left = index * 2 + 1
    if left >= len(self.list):
      return -1
    return left
  
  def get_right(self, index):
    right = index * 2 + 2
    if right >= len(self.list):
      return -1
    return right
    
  def print(self):
    print(self.list)
# test code
heap = Heap()
heap.insert(5)
heap.insert(3)
heap.insert(4)
heap.insert(1)
heap.insert(7)
heap.insert(2)
heap.insert(3)
heap.insert(6)
heap.print()
heap.pop()
heap.print()
heap.pop()
heap.print()
heap.pop()
heap.print()