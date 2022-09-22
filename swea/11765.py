#  화물도크
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    se = [list(map(int, input().split())) for _ in range(N)]
    se.sort(key=lambda x: (x[1], x[0]))
    last_time = se[0][1]
    cnt = 1
    for i in range(1, N):
        if se[i][0] >= last_time:
            last_time = se[i][1]
            cnt += 1
    print(f'#{tc} {cnt}')
