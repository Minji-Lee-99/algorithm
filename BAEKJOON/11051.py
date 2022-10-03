# 이항계수

# 시간초과
# def comb(n, r):
#     if r > n:
#         return 0
#     if r == 1 or n - r == 1:
#         return n
#     if r == 0 or n == r:
#         return 1
#     ans = comb(n - 1, r - 1) + comb(n - 1, r)
#     return ans


# 파스칼의 삼각형
# 256ms
n, r = map(int, input().split())
memo = [[0] * (n + 1) for _ in range(n + 1)]
memo[0][0] = memo[1][0] = memo[1][1] = 1
for i in range(2, n + 1):
    for j in range(i + 1):
        if j > 0 or j < i:
            memo[i][j] = memo[i - 1][j] + memo[i - 1][j - 1]
        else:
            memo[i][j] = 1
print(memo[n][r] % 10007)



