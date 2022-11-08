# 이분탐색
def solution(n, times):
    answer = max(times) * n  # 최악의 경우 저장(가장 느린 곳에서 모든 사람이 접수하는 경우)
    s = 0
    e = answer
    while s <= e:  # 역전되기 전까지 실행
        mid = (s + e) // 2
        p = sum(map(lambda x: mid // x, times))  # mid시간이 주어졌을 때, 몇명이 통과하는지 계산
        if p >= n:  # 만약 mid시간에 통과할 수 있는 사람이 주어진 사람보다 많다면
            answer = min(mid, answer)  # answer갱신(꼭 p==n인 경우만 답이 되지는 않기 때문)
            e = mid - 1
        else:
            s = mid + 1
    return answer


print(solution(6, [7, 10]))
print(solution(10, [6, 8, 10]))