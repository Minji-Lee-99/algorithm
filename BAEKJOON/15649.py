# N과 M(일반 순열)
def perm(n, k):
    if n == k:
        print(*p)
    else:
        for i in range(1, N + 1):
            if not visited[i]:
                visited[i] = True
                p[k] = i
                perm(n, k + 1)
                visited[i] = False


N, M = map(int, input().split())
visited = [False] * (N + 1)
p = [0] * M
perm(M, 0)