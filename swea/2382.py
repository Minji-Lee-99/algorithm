# 미생물 격리
T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())  # 가로 길이, 격리 시간, 군집 개수
    cnts = [[0] * N for _ in range(N)]  # 위치별 군집의 개수
    now = [list(map(int, input().split())) for _ in range(K)]  # 현재 군집의 위치, 방향, 개수
    next = []  # 1시간 후 군집의 위치, 방향, 개수
    cd = [0, 2, 1, 4, 3]
    di = [0, -1, 1, 0, 0]
    dj = [0, 0, 0, -1, 1]
    while M:
        # 다음 위치 cnts에 표기, next 리스트에 다음 위치 넣어주기
        for x, y, k, d in now:
            x, y = x + di[d], y + dj[d]
            cnts[x][y] += 1  # 움직인 후의 개수를 cnts에 표기
            next.append([x, y, k, d])
        now.clear()
        for i in range(len(next)):
            # 약품에 닿았을 때
            if next[i][0] == 0 or next[i][0] == N - 1 or next[i][1] == 0 or next[i][1] == N - 1:
                next[i][3] = cd[next[i][3]]  # 방향 바꾸기
                next[i][2] = next[i][2] // 2  # 개수 절반
            # 합쳐졌을 때
            elif cnts[next[i][0]][next[i][1]] > 1:
                max_idx = i
                sum_k = next[i][2]
                for j in range(i + 1, len(next)):
                    if next[i][0] == next[j][0] and next[i][1] == next[j][1]:
                        sum_k += next[j][2]
                        if next[max_idx][2] < next[j][2]:  # 개수가 가장 많은 군집 구하기
                            max_idx = j
                next[i][2] = sum_k
                next[i][3] = next[max_idx][3]
            # 미생물 개수가 0이 아니고 합쳐진 것이 아닌 경우만 넣어주기
            if cnts[next[i][0]][next[i][1]] and next[i][2]:
                now.append(next[i])
            # cnts 초기화 해주기
            cnts[next[i][0]][next[i][1]] = 0
        next.clear()
        M -= 1
    ans = 0
    for i in range(len(now)):
        ans += now[i][2]
    print(f'#{tc} {ans}')