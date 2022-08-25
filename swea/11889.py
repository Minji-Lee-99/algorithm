# 노드의 개수
from collections import deque


def bfs(s, g):
    visited = [0] * (v + 1)
    visited[s] = 1
    q = deque([s])
    while q:
        n = q.popleft()
        if n == g:
            return visited[g] - 1
        for w in adj[n]:
            if not visited[w]:
                visited[w] = visited[n] + 1
                q.append(w)
    return 0


T = int(input())
for tc in range(1, T + 1):
    v, e = map(int, input().split())
    adj = [[] for _ in range(v + 1)]
    for i in range(e):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)
    s, g = map(int, input().split())
    print(f'#{tc} {bfs(s, g)}')
