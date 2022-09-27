# N과 M(중복 순열)
def perm(n, k):
    if k == n:
        print(*p)
    else:
        for i in range(N):
            p[k] = arr[i]
            perm(n, k + 1)


N, M = map(int, input().split())
arr = [i for i in range(1, N + 1)]
p = [0] * M
perm(M, 0)
