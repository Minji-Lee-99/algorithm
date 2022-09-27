# N과 M(일반 순열인데, 고른 수들이 오름차순인 경우만 출력)
def perm(n, k, s):
    if n == k:
        print(*p)
    else:
        for i in range(s + 1, N + 1):
            p[k] = i
            perm(n, k + 1, i)


N, M = map(int, input().split())
p = [0] * M
perm(M, 0, 0)