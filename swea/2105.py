# 디저트 카페
def find():
    for s in range(N-1, 1, -1): # 사각형의 크기를 결정(사각형의 i+j는 n보다 항상 작음)
        for i in range(1, s):  # i는 사각형의 왼쪽 길이, j는 오른쪽 길이
            j = s - i
            for x in range(0, N - s):  # x, y좌표 결정(i, j의 크기에 따라서 가능한 좌표만 실행)
                for y in range(i, N - j):
                    # 해당 좌표에 중복값이 없는지 확인
                    check = {arr[x][y]}
                    nx, ny = x, y
                    for m in range(j):
                        nx, ny = nx + dx[1], ny + dy[1]
                        check.add(arr[nx][ny])
                    for n in range(i):
                        nx, ny = nx + dx[2], ny + dy[2]
                        check.add(arr[nx][ny])
                    for m in range(j):
                        nx, ny = nx + dx[3], ny + dy[3]
                        check.add(arr[nx][ny])
                    for n in range(i - 1):
                        nx, ny = nx + dx[0], ny + dy[0]
                        check.add(arr[nx][ny])
                    if len(check) == s * 2:
                        return s * 2
    return -1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dx = [-1, 1, 1, -1]
    dy = [1, 1, -1, -1]
    print(f'#{tc} {find()}')


# dfs로 풀기
def dfs(x, y, dir, cnt):
    global result
    nx, ny = x + dx[dir], y + dy[dir]

    # 출발점에 도착한 경우
    if nx == sx and ny == sy:
        result = max(result, cnt)
        return

    # 인덱스 체크
    if 0 <= nx < N and 0 <= ny < N and visited[arr[nx][ny]] == 0:
        visited[arr[nx][ny]] = 1
        # 가던 방향으로 계속 가기
        dfs(nx, ny, dir, cnt+1)
        # 방향 전환
        if dir < 3:
            dfs(nx, ny, dir+1, cnt+1)
        visited[arr[nx][ny]] = 0


dx = [1, 1, -1, -1]  # 우하, 좌하, 좌상, 우상
dy = [1, -1, -1, 1]
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * 101  # 카페 메뉴
    result = -1
    for i in range(N):
        for j in range(N):
            sx, sy = i, j
            visited[arr[i][j]] = 1
            dfs(i, j, 0, 1)
            visited[arr[i][j]] = 0
    print(result)