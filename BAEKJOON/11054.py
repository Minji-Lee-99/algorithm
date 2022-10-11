# 가장 긴 바이토닉 수열
N = int(input())
arr = list(map(int, input().split()))
fore = [1] * N
back = [1] * N

# 정방향의 최장증가수열 구하기
for i in range(1, N):
    for j in range(i):
        if arr[i] > arr[j]:
            fore[i] = max(fore[i], fore[j] + 1)

# 반대 방향
for i in range(N - 2, -1, -1):
    for j in range(i + 1, N):
        if arr[i] > arr[j]:
            back[i] = max(back[i], back[j] + 1)

# 최대 길이 계산
max_sum = fore[0] + back[0]
for i in range(1, N):
    ssum = fore[i] + back[i]
    max_sum = max(ssum, max_sum)
print(max_sum - 1)
