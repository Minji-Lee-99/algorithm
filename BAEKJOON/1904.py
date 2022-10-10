# 01타일
# 점화식 f(n) = f(n - 2) + f(n - 1)
def f(n):
    for i in range(3, n + 1):
        memo[i] = (memo[i - 1] + memo[i - 2]) % 15746
    return memo[n]


n = int(input())
memo = [0] * 1000001
memo[0] = memo[1] = 1
memo[2] = 2
print(f(n) % 15746)
