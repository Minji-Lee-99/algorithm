import sys
from collections import deque
sys.stdin = open("input_1227.txt", "r")


def bfs(v):
    visited[v[0]][v[1]] = 1
    q = deque([v])
    while q:
        n = q.popleft()
        if arr[n[0]][n[1]] == 3:
            return 1
        for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            ni, nj = n[0] + di, n[1] + dj
            if 0 <= ni < 100 and 0 <= nj < 100 and arr[ni][nj] != 1 and not visited[ni][nj]:
                q.append([ni, nj])
                visited[ni][nj] = 1
    return 0


N = 100
for _ in range(10):
    tc = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    print(f'#{tc} {bfs([1, 1])}')




# 방법1 시간이 굉장히 오래 걸림
# 아마 in 연산자 사용, 그리고 visited를 미리 선언하지 않고 계속 append한 것 때문이 아닐까?
# def bfs(miro):
#     visited = []
#     queue = deque([(1, 1)])
#     while queue:
#         n = queue.popleft()
#         if n not in visited:
#             visited.append(n)
#             for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
#                 nx = n[0] + dx
#                 ny = n[1] + dy
#                 if 0 <= nx < N and 0 <= ny < N:
#                     if miro[nx][ny] == 3:
#                         return 1
#                     elif miro[nx][ny] == 0 and (nx, ny) not in visited:
#                         queue.append((nx, ny))
#     return 0
#
#
# N = 100
# for _ in range(10):
#     tc = int(input())
#     miro = [list(map(int, list(input()))) for _ in range(N)]
#     print(f'#{tc} {bfs(miro)}')