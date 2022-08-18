# 종이붙이기
# DP
# f(N) = f(N - 20) * 2 + f(N - 10)

memo = [0] * 31
memo[0] = memo[1] = 1
memo[2] = 3
for i in range(3, 31):
    memo[i] = memo[i - 2] * 2 + memo[i - 1]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    N = N // 10
    print(f'#{tc} {memo[N]}')
