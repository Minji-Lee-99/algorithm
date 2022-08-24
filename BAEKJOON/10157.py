# 자리배정

x, y = map(int, input().split())  # x가 행, y가 열
target = int(input())
arr = [[0] * y for i in range(x)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
idx = i = j = 0
flag = 0
# 번호가 좌석보다 더 큰 경우엔 계산하지 않고 0 출력
if target > x * y + 1:
    print(0)
else:
    for k in range(1, x * y + 1):
        # 좌석에 대기번호 넣어주기
        arr[i][j] = k
        # 만약에 현재 대기번호가 목표 번호라면 좌석 번호 출력
        if k == target:
            print(i + 1, j + 1)
            break
        # 다음 대기번호가 들어갈 좌석 번호 구하기
        while 1:
            # 현재 방향으로 진행할 경우 좌석이 유효한지 확인
            nx, ny = i + dx[idx], j + dy[idx]
            if 0 <= nx < x and 0 <= ny < y and arr[nx][ny] == 0:
                i, j = nx, ny
                break
            # 유효하지 않으면 방향 갱신
            else:
                idx = (idx + 1) % 4