# 최소합
# dfs로 풀기
def dfs(i, j):
    for di, dj in [[0, 1], [1, 0]]:
        ni, nj = i + di, j + dj
        if 0 <= ni < N and 0 <= nj < N:
            if visited[ni][nj] == 0 or visited[ni][nj] > visited[i][j] + arr[ni][nj]:
                visited[ni][nj] = visited[i][j] + arr[ni][nj]
                dfs(ni, nj)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    visited[0][0] = arr[0][0]
    dfs(0, 0)
    print(f'#{tc} {visited[N - 1][N - 1]}')

# 순열로 풀기!
# def perm(n, k, s, x, y):
#     global ans
#     if ans < s:
#         return
#     if n == k:
#         if ans > s:
#             ans = s
#     else:
#         for i in range(2):  # 왼쪽 아래쪽을 모두 후보로 하되
#             if left[i] > 0:  # 남은 개수가 있을 때만 실행
#                 left[i] -= 1
#                 p[k] = i
#                 perm(n, k + 1, s + arr[x + i][y + abs(i - 1)], x + i, y + abs(i - 1))
#                 left[i] += 1
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     left = [N - 1, N - 1]  # 아래쪽 왼쪽 남은 개수
#     p = [0] * ((N - 1) * 2)
#     ans = 10 * 13 * 13
#     perm(len(p), 0, arr[0][0], 0, 0)
#     print(ans)


