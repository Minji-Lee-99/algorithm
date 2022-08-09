# 구간합

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    max_n = 0
    min_n = 10000 * M
    for i in range(0, N - M + 1):
        temp = 0
        for j in range(M):
            temp += nums[i + j]
        print(temp, max_n, min_n)
        if temp > max_n:
            max_n = temp
        if temp < min_n:
            min_n = temp
    print(f'#{test_case} {max_n - min_n}')