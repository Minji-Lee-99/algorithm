# 새로운 버스 노선

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    bus = [list(map(int, input().split())) for _ in range(N)]
    bs = [0] * 1001
    for i in range(N):
        if bus[i][0] == 1:  # 일반 버스
            for j in range(bus[i][1], bus[i][2] + 1):
                bs[j] += 1
        elif bus[i][0] == 2:  # 급행
            if bus[i][1] % 2:  # 홀수
                for j in range(bus[i][1], bus[i][2] + 1):
                    if j % 2:  # 짝수
                        bs[j] += 1
            else:
                for j in range(bus[i][1], bus[i][2] + 1):
                    if j % 2 == 0:
                        bs[j] += 1
        else:   # 광역
            if bus[i][1] % 2:    # 홀수
                for j in range(bus[i][1], bus[i][2] + 1):
                    if j % 3 == 0 and j % 10 != 0:
                        bs[j] += 1
            else:   # 짝수
                for j in range(bus[i][1], bus[i][2] + 1):
                    if j % 4 == 0:
                        bs[j] += 1
    print(f'#{tc} {max(bs)}')

