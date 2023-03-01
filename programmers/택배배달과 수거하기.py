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

def solution1(cap, n, deliveries, pickups):
    answer = 0
    return answer


print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))
print(solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]))
