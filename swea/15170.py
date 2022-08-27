# 낚시터 자리잡기


def perm(s, k):
    if s == k - 1:
        place = [0] * (N + 1)  # 낚시터 자리
        place[0] = 1
        find_ans(place, 1, 0)
    else:
        for i in range(s, k):
            gate[i], gate[s] = gate[s], gate[i]
            perm(s+1, k)
            gate[i], gate[s] = gate[s], gate[i]


def find_ans(place, k, total):
    global ans
    if k == 4:  # 베이스 케이스
        if total < ans:
            ans = total
        return
    else:
        # 각 사람마다 자리 탐색
        for i in range(gate[k][1]):
            # 갈 수 있는 자리 찾기
            if place[gate[k][0]] == 0:  # 바로 게이트 앞자리에 앉는 경우
                tg = [gate[k][0]]
            else:   # 양방향 탐색이 필요한 경우
                tg = []
                for di in [-1, 1]:
                    ni = gate[k][0] + di
                    level = 1
                    while 0 <= ni < N + 1 and place[ni]:
                        level += 1
                        ni = gate[k][0] + di * level
                    if 0 <= ni < N + 1:
                        tg.append(ni)
            # 마지막 사람의 경우
            if i == gate[k][1] - 1:
                # 갈 수 있는 자리가 1자리라면 그냥 거기 넣기
                if len(tg) < 2:
                    total += abs(tg[0] - gate[k][0]) + 1
                    place[tg[0]] = 1
                    find_ans(place, k + 1, total)
                # 갈 수 있는 자리가 두자리
                else:
                    a = abs(tg[0] - gate[k][0]) + 1
                    b = abs(tg[1] - gate[k][0]) + 1
                    # 두 자리 모두 거리가 같다면 두자리 모두 고려해보야 함
                    if a == b:
                        # a에 채우는 경우
                        place2 = place[::]
                        place2[tg[0]] = 1
                        find_ans(place2, k + 1, total + a)
                        # b에 넣는 경우
                        place2 = place[::]
                        place2[tg[1]] = 1
                        find_ans(place2, k + 1, total + b)
                    # a가 더 작은 경우엔 그냥 a에 넣는다.
                    elif b > a:
                        total += a
                        place[tg[0]] = 1
                        find_ans(place, k + 1, total)
                    # b가 더 작은 경우엔 그냥 b에 넣는다.
                    else:
                        total += b
                        place[tg[1]] = 1
                        find_ans(place, k + 1, total)
            # 마지막 사람들이 아닌 경우들
            # 갈 수 있는 자리가 1자리라면 그냥 거기 넣기
            elif len(tg) < 2:
                total += abs(tg[0] - gate[k][0]) + 1
                place[tg[0]] = 1
            # 여러 자리인 경우 더 작은 곳에 넣기,
            else:
                a = abs(tg[0] - gate[k][0]) + 1
                b = abs(tg[1] - gate[k][0]) + 1
                if b > a:
                    total += a
                    place[tg[0]] = 1
                else:
                    total += b
                    place[tg[1]] = 1


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    gate = [[0, 0]]    # 게이트 순서
    ans = N ** 2     # 정답
    for i in range(3):
        a, b = map(int, input().split())
        gate.append([a, b])
    perm(1, 4)
    print(f'#{tc} {ans}')
