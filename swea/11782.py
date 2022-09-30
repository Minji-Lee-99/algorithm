# 최소 비용
# from collections import deque
#
#
# def bfs():
#     q = deque()
#     q.append([0, 0])
#     D[0][0] = 0
#     while q:
#         x, y = q.popleft()
#         for dx, dy in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
#             nx, ny = x + dx, y + dy
#             if 0 <= nx < N and 0 <= ny < N:
#                 if arr[x][y] < arr[nx][ny]:
#                     new_d = D[x][y] + arr[nx][ny] - arr[x][y] + 1
#                     if D[nx][ny] > new_d:
#                         D[nx][ny] = new_d
#                         q.append([nx, ny])
#                 else:
#                     if D[nx][ny] > D[x][y] + 1:
#                         D[nx][ny] = D[x][y] + 1
#                         q.append([nx, ny])
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     D = [[2000] * N for _ in range(N)]
#     bfs()
#     print(f'#{tc} {D[N - 1][N - 1]}')

# 다익스트라로 풀기
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
#         if x == N - 1 and y == N - 1:  # 도착지점에 도착한 경우
#             return
#         for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
#             ni, nj = ui + di, uj + dj
#             if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
#                 if arr[ni][nj] > arr[ui][uj]:
#                     D[ni][nj] = min(D[ni][nj], D[ui][uj] + arr[ni][nj] - arr[ui][uj] + 1)
#                 else:
#                     D[ni][nj] = min(D[ni][nj], D[ui][uj] + 1)
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


# 다익스트라 + heap
import heapq


def dijkstra(x, y):
    D[x][y] = 0
    heap = []
    heapq.heappush(heap, (D[x][y], x, y))  # 가중치, x, y
    while heap:
        # 최솟값 찾기
        d, ui, uj = heapq.heappop(heap)
        visited[ui][uj] = 1
        if ui == N - 1 and uj == N - 1:  # 도착지점이 클라우드에 들어간 경우
            return
        for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            ni, nj = ui + di, uj + dj
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
                diff = 0
                if arr[ni][nj] > arr[ui][uj]:
                    diff = arr[ni][nj] - arr[ui][uj]
                if D[ni][nj] > D[ui][uj] + diff + 1:
                    D[ni][nj] = D[ui][uj] + diff + 1
                    heapq.heappush(heap, (D[ni][nj], ni, nj))


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    D = [[2000] * N for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    dijkstra(0, 0)
    print(f'#{tc} {D[N - 1][N - 1]}')
