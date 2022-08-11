# 특별한 정렬
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    for i in range(N - 1):
        idx = i
        if i % 2:
            for j in range(i, N):
                if arr[j] < arr[idx]:
                    idx = j
        else:
            for j in range(i, N):
                if arr[j] > arr[idx]:
                    idx = j
        arr[i], arr[idx] = arr[idx], arr[i]
    print(f'#{test_case}', end=' ')
    for i in range(10):
        print(arr[i], end=' ')
    print('\n', end='')
