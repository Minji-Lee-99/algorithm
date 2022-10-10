# 파도반 수열
def f(n):
    if n < 6 or memo[n] != 0:
        return memo[n]
    else:
        memo[n] = f(n - 1) + f(n - 5)
        return memo[n]


memo = [0] * 101
memo[0] = memo[1] = memo[2] = memo[3] = 1
memo[4] = memo[5] = 2
T = int(input())
for _ in range(T):
    n = int(input())
    print(f(n))

