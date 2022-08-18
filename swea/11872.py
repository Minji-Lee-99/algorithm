# 그래프 경로

# 방법 1
# 한번에 간선 다 넣기 + 반복문
def dfs(v):
    stack = [v]
    visited = [False] * (V + 1)
    while stack:
        n = stack.pop()
        if n == G:
            return 1
        if not visited[n]:
            visited[n] = True
            for w in adj[n]:
                stack.append(w)
    return 0


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    adj = [[] for _ in range((V + 1))]
    for i in range(E):
        a, b = map(int, input().split())
        adj[a].append(b)
    S, G = map(int, input().split())
    print(f'#{tc} {dfs(S)}')
