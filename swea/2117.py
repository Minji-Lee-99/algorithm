# 홈 방범 서비스

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    house = []
    ans = 0
    # house에 집의 좌표 넣기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                house.append([i, j])
    for k in range(1, N + 3):
        for i in range(N):
            for j in range(N):
                cnt = 0
                for x, y in house:
                    if abs(i-x) + abs(j-y) < k:
                        cnt += 1
                if k * k + (k-1) * (k-1) <= cnt * M and cnt > ans:
                    ans = cnt
    print(f'#{tc} {ans}')

