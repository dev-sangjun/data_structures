class Trie:
  head = {}

  def add(self, word):
    cur = self.head
    for c in word:
      if c not in cur:
        cur[c] = {}
      cur = cur[c]
    cur['*'] = True
  
  def contains(self, word):
    cur = self.head
    for c in word:
      if c not in cur:
        return False
      cur = cur[c]
    if '*' in cur:
      return True
    else:
      return False

# test code

trie = Trie()
trie.add('hello')
trie.add('he')

print(trie.contains('he'))
print(trie.contains('hel'))
print(trie.contains('hello'))