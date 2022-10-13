# 가장 긴 바이토닉 수열
N = int(input())
arr = list(map(int, input().split()))
fore = [1] * N  # i번째 수까지 봤을 때 중가하는 수열의 개수 저장 리스트
back = [1] * N  # 반대 방향으로 봤을 때 증가하는 수열의 개수 저장 리스트

# 정방향의 증가수열 구하기
for i in range(1, N):
    for j in range(i):
        if arr[i] > arr[j]:
            fore[i] = max(fore[i], fore[j] + 1)

# 반대 방향으로 봤을 때, 증가수열 구하기
for i in range(N - 2, -1, -1):
    for j in range(i + 1, N):
        if arr[i] > arr[j]:
            back[i] = max(back[i], back[j] + 1)

# 최대 길이 계산
# i를 기준으로 정방향에서 증가하는 수열의 개수와 반대 방향에서 증가하는 수열의 개수를 더했을 때, 가장 큰 값이 가장 큰 바이토닉 수열
max_sum = fore[0] + back[0]
for i in range(1, N):
    ssum = fore[i] + back[i]
    max_sum = max(ssum, max_sum)
print(max_sum - 1)  # i번 숫자는 2번 더해지기 때문에 1번 빼주기
