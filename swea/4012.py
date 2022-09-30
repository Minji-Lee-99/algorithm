# 요리사
def comb(n, k, s):
    global ans
    if n == k:
        total1 = 0
        for i in range(N):
            if t[i]:
                for j in range(N):
                    if t[i]:
                        total1 += arr[i][j]
        total2 = 0
        for i in range(N):
            if not t[i]:
                for j in range(N):
                    if not t[i]:
                        total2 += arr[i][j]
        ans = min(ans, abs(total1 - total2))

    else:
        for i in range(s, N):
            t[i] = 1
            comb(n, k + 1, i + 1)
            t[i] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    t = [0] * N
    t[0] = 1
    ans = 1e10
    comb(N // 2, 1, 1)
