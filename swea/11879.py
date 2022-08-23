# 미로

def dfs(x, y):
    global flag
    visited[x][y] = True
    if arr[x][y] == 3:
        flag = 1
        return
    for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < N and 0 <= ny < N and (arr[nx][ny] == 0 or arr[nx][ny] == 3) and not visited[nx][ny]:
            dfs(nx, ny)
    return


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
    visited = [[False] * N for _ in range(N)]
    flag = 0
    dfs(i, j)
    print(f'#{tc} {flag}')

