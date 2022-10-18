# 핀볼 게임

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    tri = [[], [3, 0, 1, 2], [2, 3, 1, 0], [1, 2, 3, 0], [3, 2, 0, 1]]  # 상: 0, 하: 3, 좌: 1, 우: 2
    hole = {6: [], 7: [], 8: [], 9: [], 10: []}
    visited = [[0] * N for _ in range(N)]
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]

    # 웜홀 정보
    for i in range(N):
        for j in range(N):
            if 6 <= arr[i][j] <= 10:
                hole[arr[i][j]].append((i, j))

    # 찾기
    ans = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0 and not visited[i][j]:  # 0이면 출발점이 될 수 있음
                visited[i][j] = 1
                for m in range(4):  # 4방향으로 가는 경우를 모두 봐주어야 함.
                    d = m
                    cnt = 0
                    x, y = i, j
                    while True:
                        nx, ny = dx[d] + x, dy[d] + y
                        if (nx, ny) == (i, j) or arr[nx][ny] == -1:
                            ans = max(ans, cnt)
                            break
                        if nx < 0 or nx >= N or ny < 0 or ny >= N or arr[nx][ny] == 5:
                            ans = max(ans, cnt * 2 + 1)
                            break
                        if 1 <= arr[nx][ny] <= 4:
                            d = tri[arr[nx][ny]][d]
                            cnt += 1
                        x, y = dx, dy
                        if 6 <= arr[nx][ny] <= 10:
                            if hole[arr[nx][ny]][0] == (nx, ny):
                                x, y = hole[arr[nx][ny]][1]
                            else:
                                x, y = hole[arr[nx][ny]][0]
    print(f'#{tc} {ans}')















