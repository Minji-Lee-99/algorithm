# 미로의 거리
from collections import deque


def bfs(v):
    q = deque([v])
    visited = [[0] * N for _ in range(N)]
    visited[v[0]][v[1]] = 1
    while q:
        v = q.popleft()
        if arr[v[0]][v[1]] == 3:
            return visited[v[0]][v[1]] - 2
        for di, dj in [[1, 0], [0, 1], [0, -1], [-1, 0]]:
            ni, nj = v[0] + di, v[1] + dj
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and arr[ni][nj] != 1:
                visited[ni][nj] = visited[v[0]][v[1]] + 1
                q.append([ni, nj])
    return 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    i = j = 0
    while i < N and j < N:
        if arr[i][j] == 2:
            break
        j += 1
        i += j // N
        j %= N
    print(f'#{tc} {bfs([i, j])}')
