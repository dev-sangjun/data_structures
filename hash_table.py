from linked_list import LinkedList

class Element:
  def __init__(self, key, value):
    self.key = key
    self.value = value
  
  def __str__(self):
    return '(key: {}, value: {})'.format(self.key, self.value)
  
  def __repr__(self):
    return '(key: {}, value: {})'.format(self.key, self.value)


class HashTable:
  def __init__(self, size):
    self.size = size
    self.table = [LinkedList() for _ in range(size)]

  def insert(self, key, value):
    # check if the key exists in the hash table
    element = self.get(key)
    if element == None:
      index = hash(key) % self.size
      self.table[index].append(Element(key, value))
    else:
      element.value = value

  def remove(self, key):
    element = self.get(key)
    if element != None:
      index = hash(key) % self.size
      linked_list = self.table[index]
      for i in range(linked_list.length):
        if linked_list.get(i).key == key:
          linked_list.remove(i)
          return

  def get(self, key):
    index = hash(key) % self.size
    linked_list = self.table[index]
    for i in range(linked_list.length):
      if linked_list.get(i).key == key:
        return linked_list.get(i)
    return None    

  def print(self):
    for i in range(self.size):
      print(self.table[i])

# test code
hash_table = HashTable(10)

