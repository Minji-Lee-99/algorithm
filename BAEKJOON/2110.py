# 공유기 설치
N, M = map(int, input().split())
arr = []

for _ in range(N):
    arr.append(int(input()))
arr.sort()

s = 1  # 최소거리
e = arr[-1] - arr[0]  # 최대거리
while s <= e:
    mid = (s + e) // 2  # 기준 거리
    cnt = 1  # 선택된 집의 개수
    bf = arr[0]  # 제일 첫번째 집은 무조건 선택하고 시작
    for i in range(1, len(arr)):
        if arr[i] - bf >= mid:  # 이전에 선택된 집으로부터 기준거리 떨어진 집만 선택하기
            cnt += 1
            bf = arr[i]
    if cnt >= M:  # 선택된 집의 개수가 선택해야 하는 집보다 크거나 같으면 result에 결과 저장해두고, 기준거리 더 크게 만들기
        result = mid  # 항상 result는 더 큰 mid로만 갱신될 수 있기 때문에 조건문을 적어주지 않아도 됨.
        s = mid + 1  # mid가 result에 저장되어 있기 때문에 mid + 1해도 문제 X
    else:  # 선택된 집의 개수가 선택해야 하는 집보다 작으면, 기준거리를 더 작게 만들기
        e = mid - 1
print(result)


