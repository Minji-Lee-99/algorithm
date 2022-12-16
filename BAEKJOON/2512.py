# 백준 2512 예산
N = int(input())
arr = list(map(int, input().split()))
budget = int(input())

s = 0  # 상한액의 최솟값
e = max(arr)  # 상한액의 최댓값
answer = 0
while s <= e:
    mid = (s + e) // 2  # 상한액
    ssum = 0
    max_budget = 0
    for i in range(N):
        if arr[i] >= mid:  # 요청 예산이 상한액보다 크거나 같으면 상한액 배정
            ssum += mid
            max_budget = max(max_budget, mid)  # 가장 큰 배정 예산 저장
        else:  # 요청 예산이 상한액보다 작으면 요청 예산 배정
            max_budget = max(arr[i], max_budget)  # 가장 큰 배정 예산을 저장
            ssum += arr[i]
    if ssum <= budget:  # 현재 상한액에서 계산한 총 예산이 주어진 예산보다 작거나 같다면 상한액을 더 키워서 확인하기
        s = mid + 1
        answer = max_budget
    else:  # 현재 상한액에서 계산한 총 예산이 주어진 예산보다 작으면 상한액을 더 낮춰서 확인하기
        e = mid - 1
print(answer)
