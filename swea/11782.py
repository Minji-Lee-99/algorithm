# 최소 비용
from collections import deque


def bfs():
    q = deque()
    q.append([0, 0])
    D[0][0] = 0
    while q:
        x, y = q.popleft()
        for dx, dy in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if arr[x][y] < arr[nx][ny]:
                    new_d = D[x][y] + arr[nx][ny] - arr[x][y] + 1
                    if D[nx][ny] > new_d:
                        D[nx][ny] = new_d
                        q.append([nx, ny])
                else:
                    if D[nx][ny] > D[x][y] + 1:
                        D[nx][ny] = D[x][y] + 1
                        q.append([nx, ny])


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    D = [[2000] * N for _ in range(N)]
    bfs()
    print(f'#{tc} {D[N - 1][N - 1]}')

# 제한 시간 초과
# def dijkstra(x, y):
#     D[x][y] = 0
#     for _ in range(N ** 2):
#         # 최솟값 찾기
#         min_v = 2000
#         for i in range(N):
#             for j in range(N):
#                 if visited[i][j] == 0 and min_v > D[i][j]:
#                     min_v = D[i][j]
#                     ui, uj = i, j
#         visited[ui][uj] = 1
#         for di, dj in [[1, 0], [0, 1]]:
#             ni, nj = ui + di, uj + dj
#             if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
#                 D[ni][nj] = min(D[ni][nj], D[ui][uj] + abs(arr[ni][nj] - arr[ui][uj]) + 1)
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     D = [[2000] * N for _ in range(N)]
#     visited = [[0] * N for _ in range(N)]
#     dijkstra(0, 0)
#     print(f'#{tc} {D[N - 1][N - 1]}')
