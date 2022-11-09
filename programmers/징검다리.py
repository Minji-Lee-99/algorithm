# 이분탐색
def solution(distance, rocks, n):
    answer = 0
    s = 1
    e = distance  # 간격의 최댓값은 distance
    rocks.sort()
    rocks = [0] + rocks + [distance]
    while s <= e:
        mid = (s + e) // 2  # mid가 최소 간격
        cnt = 0  # 부순 횟수를 저장하는 변수
        temp = [0]  # 부수지 않은 돌을 저장하는 곳
        for idx in range(1, len(rocks) - 1):
            if rocks[idx] - temp[-1] < mid:  # idx위치에서 마지막 돌의 위치까지의 거리가 최소 간격 보다 작으면 해당 돌을 없애서 간격을 넓혀주어야 함
                cnt += 1  # 부순 돌 개수 카운트
                if cnt > n:  # 부순 돌의 개수가 주어진 돌의 개수보다 많으면 멈추기
                    e = mid - 1  # 이 경우 간격이 더 작아야 하는 것이기 때문에 e를 갱신
                    break
            else:  # 간격이 mid보다 크거나 같으면 돌을 그냥 두면 되기 때문에, temp에 추가해주기
                temp.append(rocks[idx])
        else:
            if rocks[-1] - temp[-1] < mid:  # 마지막 돌에서 distance까지의 간격은 mid보다 크거나 같아아 하지만, distance는 없앨 수 없기 때문에 따로 판단해주기
                e = mid - 1
            else:  # 모든 간격이 조건을 만족하는 경우
                answer = max(mid, answer)  # answer를 갱신해주기
                s = mid + 1  # 더 큰 값 중에서 조건을 만족하는 경우가 있는지 판단해주기
    return answer


print(solution(25, [2, 11, 14, 17, 21], 2))
