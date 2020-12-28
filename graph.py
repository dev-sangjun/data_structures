graph = {
  'A': ['B', 'C', 'E'],
  'B': ['A','D', 'E'],
  'C': ['A', 'F', 'G'],
  'D': ['B'],
  'E': ['A', 'B','D'],
  'F': ['C'],
  'G': ['C']
}

def bfs(graph, target):
  visited = {}
  queue = []
  queue.append('A')
  visited['A'] = True
  while queue:
    cur = queue.pop(0)
    for node in graph[cur]:
      if node == target:
        print('found {}'.format(target))
        return True
      if node not in visited:
        queue.append(node)
        visited[node] = True
    print('cur: {}, queue: {}, visited: {}'.format(cur, queue, visited))
  return False

def dfs(graph, target):
  visited = {}
  stack = []
  stack.append('A')
  visited['A'] = True
  while stack:
    cur = stack.pop()
    for node in graph[cur]:
      if node == target:
        print('found {}'.format(target))
        return True
      if node not in visited:
        stack.append(node)
        visited[node] = True
    print('cur: {}, queue: {}, visited: {}'.format(cur, stack, visited))
  return False

# test code
print(bfs(graph, 'E'))
print(dfs(graph, 'F'))