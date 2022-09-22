# 전자카트
def perm(n, k, s):
    global ans
    if s > ans:
        return
    if n == k:
        if s + battery[p[k-1]][p[k]] < ans:
            ans = s + battery[p[k-1]][p[k]]
    else:
        for i in range(n):
            if visited[i] == 0:
                visited[i] = 1
                p[k] = a[i]
                perm(n, k + 1, s + battery[p[k-1]][p[k]])
                visited[i] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    battery = [list(map(int, input().split())) for _ in range(N)]
    p = [0] * (N + 1)
    visited = [0] * (N + 1)
    visited[0] = visited[N] = 1
    a = [i for i in range(0, N)] + [0]
    ans = 1000
    perm(N, 1, 0)
    print(ans)

