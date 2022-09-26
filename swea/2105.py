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
