# 격자판 이어 붙이기
def dfs(num, p):
    if len(num) == 7:
        ans.add(num)
        return
    else:
        p1, p2 = p
        for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            ni, nj = p1 + di, p2 + dj
            if 0 <= ni < 4 and 0 <= nj < 4:
                dfs(num + arr[ni][nj], (ni, nj))


T = int(input())
for tc in range(1, T + 1):
    arr = [input().split() for _ in range(4)]
    ans = set()
    for i in range(4):
        for j in range(4):
            dfs(arr[i][j], (i, j))
    print(f'#{tc} {len(ans)}')
