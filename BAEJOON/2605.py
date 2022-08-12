N = int(input())
arr = list(map(int, input().split()))
std = list(range(1, N + 1))

for i in range(1, N):
    for j in range(arr[i]):
        std[i - j], std[i - j - 1] = std[i - j - 1], std[i - j]

print(*std)
