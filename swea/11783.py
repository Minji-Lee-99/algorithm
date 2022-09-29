# 최소 이동 거리
def dijkstra(s):
    D[s] = 0
    for _ in range(V + 1):
        min_v = 100
        for i in range(V + 1):
            if visited[i] == 0 and min_v > D[i]:
                min_v = D[i]
                u = i
        visited[u] = 1
        for i in range(V + 1):
            if visited[i] == 0 and adjM[u][i]:
                D[i] = min(D[i], D[u] + adjM[u][i])


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    adjM = [[0] * (V + 1) for _ in range(V + 1)]
    D = [100] * (V + 1)
    visited = [0] * (V + 1)
    for _ in range(E):
        s, e, w = map(int, input().split())
        adjM[s][e] = w
    dijkstra(0)
    print(f'#{tc} {D[V]}')
