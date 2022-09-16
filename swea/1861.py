# 정사각형 방
def dfs(i, j):
    temp = 1
    if visited[i][j]:
        return visited[i][j]
    for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        ni, nj = i + di, j + dj
        if 0 <= ni < N and 0 <= nj < N and arr[i][j] + 1 == arr[ni][nj]:
            temp += dfs(ni, nj)
    visited[i][j] = temp
    return temp


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    maxV = ans = 0
    for i in range(N):
        for j in range(N):
            t = dfs(i, j)
            if t > maxV or (t == maxV and ans > arr[i][j]):
                maxV = t
                ans = arr[i][j]
    print(f'#{tc} {ans} {maxV}')


