import math


# 예제
# 번호: 1 2 3 4 5
# 배달: 1 0 3 1 2
# 픽업: 0 3 0 4 0
# 배달 누적: 7 6 6 3 2
# 픽업 누적: 7 7 4 4 0
# 위 경우에서 cap이 4라면 배달 누적의 경우 5, 3번 집에서 갱신, 픽업 누적의 경우 4, 2에서 갱신
# 더 먼 곳을 기준으로 해야 하기 때문에 (5 + 3) * 2
def solution(cap, n, deliveries, pickups):
    answer = 0
    d_sum = 0  # 누적 배달 개수 합
    p_sum = 0  # 누적 픽업 개수 합
    now = 0  # 현재 왕복 횟수
    for i in range(n - 1, -1, -1):  # 가장 마지막 집에서부터 누적 개수를 확인
        d_sum += deliveries[i]  # i번째 집에 해당하는 개수 더해주기
        p_sum += pickups[i]
        temp = max(math.ceil(d_sum / cap), math.ceil(p_sum / cap))  # 현재 배달 횟수 및 픽업 횟수는 몇번을 왕복한 경우인지 체크
        if now < temp:  # 그 값이 변하는 지점이 배달을 새롭게 다시 하는 경우이므로 해당 경우에 answer값에 더해주어야 한다.
            answer += (i + 1) * (temp - now)  # 한 집에서 여러번 왕복을 해야 할 만큼의 양을 원할 수 있기 때문에 temp - now만큼 곱해준다.
            now = temp
    return answer * 2


# 15 ~ 20 case 시간초과
def solution1(cap, n, deliveries, pickups):
    answer = 0
    while True:
        del_cnt = 0
        del_pos = 0
        for i in range(n - 1, -1, -1):
            if del_cnt == cap:
                break
            if deliveries[i] == 0:
                continue
            if i + 1 > del_pos:
                del_pos = (i + 1)
            if deliveries[i] <= (cap - del_cnt):
                del_cnt += deliveries[i]
                deliveries[i] = 0
            else:
                deliveries[i] -= (cap - del_cnt)
                del_cnt = cap

        pick_cnt = 0
        pick_pos = 0
        for i in range(n - 1, -1, -1):
            if pick_cnt == cap:
                break
            if pickups[i] == 0:
                continue
            if i + 1 > pick_pos:
                pick_pos = (i + 1)
            if pickups[i] <= (cap - pick_cnt):
                pick_cnt += pickups[i]
                pickups[i] = 0
            else:
                pickups[i] -= (cap - pick_cnt)
                pick_cnt = cap
        if del_cnt == 0 and pick_cnt == 0:
            break
        answer += max(pick_pos, del_pos) * 2
    return answer


print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))
print(solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]))
