N = int(input())
arr = list(map(int, input().split()))
check = [0] * N
check_reverse = [0] * N
check[0] = check_reverse[-1] = 1

max_len = 1
for i in range(1, N):
    if arr[i] >= arr[i - 1]:
        check[i] = check[i - 1] + 1
        if check[i] > max_len:
            max_len = check[i]
    else:
        check[i] = 1

for i in range(N - 2, -1, -1):
    if arr[i] >= arr[i + 1]:
        check_reverse[i] = check_reverse[i + 1] + 1
        if check_reverse[i] > max_len:
            max_len = check_reverse[i]
    else:
        check_reverse[i] = 1

print(max_len)
