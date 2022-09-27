# 동철이의 일 분배
def perm(n, k, p):
    global ans
    if p <= ans:
        return
    if n == k:
        if ans < p:
            ans = p
        return
    for i in range(N):
        if not visited[i] and arr[k][i] != 0:
            visited[i] = True
            perm(n, k + 1, p * arr[k][i] / 100)
            visited[i] = False


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [False] * N
    ans = 0
    perm(N, 0, 1)
    print(f'#{tc} {ans * 100:.6f}')
