# DFS와 BFS

from collections import deque

def DFS(graph, stack, visited):
    if not stack:
        return visited
    else:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            temp = list(graph[n] - set(visited))
            temp.sort(reverse=True)
            stack += temp
    return DFS(graph, stack, visited)

def BFS(graph, root):
    queue = deque([root])
    visited = []
    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            temp = list(graph[n] - set(visited))
            temp.sort()
            queue += temp
    return visited

N, M, V = input().split()
graph = {}
for _ in range(int(M)):
    a, b = input().split()
    if a in graph:
        graph[a].add(b)
    else:
        graph[a] = set(b)
    if b in graph:
        graph[b].add(a)
    else:
        graph[b] = set(a)

print(' '.join(DFS(graph, [V], [])))
print(' '.join(BFS(graph, V)))


