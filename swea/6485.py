# 삼성시의 버스노선
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    routes = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    bus = [int(input()) for _ in range(P)]
    print(f'#{tc}', end=' ')
    for b in bus:
        cnt = 0
        for route in routes:
            if route[0] <= b <= route[1]:
                cnt += 1
        print(f'{cnt}', end=' ')
    print('\n', end='')