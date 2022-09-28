# 스타트와 링크
def perm(n, k, ssum1, ssum2):
    if n == k:
        print(p)
    else:
        for i in range(2):
            if cnt[i]:
                p[k] = i
                cnt[i] -= 1
                perm(n, k + 1)
                cnt[i] += 1


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt = [N // 2, N // 2]
p = [0] * N
perm(N, 0, 0, 0)
