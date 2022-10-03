# 조합
n, r = map(int, input().split())
memo = [[0] * (n + 1) for _ in range(n + 1)]
memo[0][0] = memo[1][0] = memo[1][1] = 1
for i in range(2, n + 1):
    for j in range(i + 1):
        if 0 < j < i:
            memo[i][j] = memo[i - 1][j] + memo[i - 1][j - 1]
        else:
            memo[i][j] = 1
print(memo[n][r])
