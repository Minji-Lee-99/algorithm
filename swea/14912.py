# 부분집합의 합

T = int(input())
for test_case in range(1, T + 1):
    result = 0
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(1<<n):
        temp = []
        for j in range(n):
            if i & (1<<j):
                temp.append(arr[j])
        if temp:
            total = 0
            for a in temp:
                total += a
            if total == 0:
                result = 1
                break
    print(f'#{test_case} {result}')



