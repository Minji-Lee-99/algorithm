# 최소 생산 비용
def perm(n, k, ssum):
    global ans
    if ssum > ans:
        return
    if n == k:
        ans = min(ssum, ans)
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            perm(n, k + 1, ssum + arr[k][A[i]])
            visited[i] = False


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    A = [i for i in range(N)]
    ans = 99 * 15
    visited = [False] * N
    perm(N, 0, 0)
    print(f'#{tc} {ans}')
