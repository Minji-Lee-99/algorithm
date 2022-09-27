# N과 M(중복 순열인데, 단 비내림차순이어야 함)
def perm(n, k, s):
    if k == n:
        print(*p)
    else:
        for i in range(s, N):
            p[k] = arr[i]
            perm(n, k + 1, i)


N, M = map(int, input().split())
arr = [i for i in range(1, N + 1)]
p = [0] * M
perm(M, 0, 0)
