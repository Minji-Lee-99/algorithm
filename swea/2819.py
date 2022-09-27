# 격자판 이어 붙이기
# def dfs(num, p):
#     if len(num) == 7:
#         ans.add(num)
#         return
#     else:
#         p1, p2 = p
#         for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
#             ni, nj = p1 + di, p2 + dj
#             if 0 <= ni < 4 and 0 <= nj < 4:
#                 dfs(num + arr[ni][nj], (ni, nj))
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     arr = [input().split() for _ in range(4)]
#     ans = set()
#     for i in range(4):
#         for j in range(4):
#             dfs(arr[i][j], (i, j))
#     print(f'#{tc} {len(ans)}')


# set을 안쓰고는 어떻게 할 수 있을까?
def dfs(x, y, k, num):
    global ans
    if k == 6:
        if visited[num] != tc:
            ans += 1
            visited[num] = tc
    else:
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < 4 and 0 <= ny < 4:
                dfs(nx, ny, k+1, num * 10 + arr[nx][ny])


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [False] * 100000000  # 0 ~ 9999999
T = int(input())
for tc in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(4)]
    ans = 0
    for i in range(4):
        for j in range(4):
            dfs(i, j, 0, arr[i][j])
    print(f'#{tc} {ans}')
