class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None
  
  def insert(self, val):
    if self.val == val:
      return
    elif val < self.val:
      if self.left == None:
        self.left = Node(val)
      else:
        self.left.insert(val)
    else:
      if self.right == None:
        self.right = Node(val)
      else:
        self.right.insert(val)

  def contains(self, val):
    if val == self.val:
      return True
    elif val < self.val:
      if not self.left:
        return False
      else:
        return self.left.contains(val)
    else:
      if not self.right:
        return False
      else:
        return self.right.contains(val)

  def print(self):
    if self.left:
      self.left.print()
    print('{} '.format(self.val))
    if self.right:
      self.right.print()

def checkBST(root, min, max):
  if root == None:
    return True
  if root.val < min or root.val > max:
    return False
  return checkBST(root.left, min, root.val - 1) and checkBST(root.right, root.val + 1, max)

# test code
root = Node(5)
root.insert(5)
root.insert(6)
root.insert(2)
root.insert(1)
root.print()
print(root.contains(4))
print(root.contains(1))

root_ = Node(5)
root_.left = Node(2)
root_.right = Node(1)

print(checkBST(root, float('-inf'), float('inf')))
print(checkBST(root_, float('-inf'), float('inf')))