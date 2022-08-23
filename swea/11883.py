# 배열 최소 합

def perm(k, n, ssum):
    global ans
    if ans < ssum:
        return
    if k == n:
        if ans > ssum:
            ans = ssum
    else:
        for i in range(k, n):
            num[k], num[i] = num[i], num[k]
            perm(k + 1, n, ssum + arr[k][num[k]])
            num[k], num[i] = num[i], num[k]
    return


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    num = [i for i in range(N)]
    ans = 0
    for i in range(N):
        ans += arr[i][i]
    perm(0, N, 0)
    print(f'#{tc} {ans}')
