# min max

def my_min_max(arr):
    min_n = arr[0]
    max_n = arr[0]
    for n in arr:
        if max_n < n:
            max_n = n
        elif min_n > n:
            min_n = n
    return min_n, max_n

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    n, m = my_min_max(numbers)
    print(f'#{test_case} {m - n}')