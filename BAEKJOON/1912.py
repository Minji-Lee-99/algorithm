# 연속합
N = int(input())
arr = list(map(int, input().split()))
ssum = 0
max_sum = -100000000
for i in range(N):
    if arr[i] >= 0:  # 0보다 크거나 같다면 무조건 더해줘야 함
        ssum += arr[i]
    else:  # 더해줄 값이 음수인 경우
        max_sum = max(ssum, max_sum)  # 일단 음수를 만나면 무조건 max_sum갱신
        if ssum + arr[i] < 0:  # 음수 값을 더하면 현재까지의 연속합이 0보다 작아진다면 해당 값은 더하지 않는게 맞음. 그러므로 다시 ssum을 0으로 초기화 하고 그 다음 값부더 다시보기
            ssum = 0
        else:
            ssum += arr[i]  # 더할 값이 음수이긴 해도 현재까지의 총합이 0보다 크다면 일단 더 더해보기
max_sum = max(ssum, max_sum)  # 음수를 만났을 때를 기준으로 갱신하기 때문에 마지막에 추가로 한번 더 갱신
if max_sum == 0 and ssum == 0:  # 이 경우는 음수값만 있는 경우이다.
    print(max(arr))
else:
    print(max_sum)

# 1, 11, -6, 1
# 2, -4 , 5, 6