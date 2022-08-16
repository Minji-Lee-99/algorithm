# 부분집합

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    result = 0
    for i in range(1 << 12):
        total = length = 0
        for j in range(12):
            if i & (1 << j):
                total += arr[j]
                length += 1
        if total == K and length == N:
            result += 1
    print(f'#{test_case} {result}')
