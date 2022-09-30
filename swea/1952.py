# 수영장
def dfs(n, k, ssum):
    global ans
    if ans < ssum:
        return
    if n <= k:
        ans = min(ans, ssum)
        return
    if plan[k] != 0:
        for i in range(3):
            if i == 0:
                dfs(n, k + 1, ssum + price[i] * plan[k])
            elif i == 1:
                dfs(n, k + 1, ssum + price[i])
            else:
                dfs(n, k + 3, ssum + price[i])
    else:
        dfs(n, k + 1, ssum)


T = int(input())
for tc in range(1, T + 1):
    price = list(map(int, input().split()))
    plan = list(map(int, input().split()))
    ans = price[3]
    dfs(12, 0, 0)
    print(f'#{tc} {ans}')
