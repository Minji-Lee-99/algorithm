# 달팽이 숫자

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    result = [[0 for i in range(N)] for j in range(N)]
    x = y = 0
    result[x][y] = 1
    index = 0
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    for i in range(2, N ** 2 + 1):
        while 1:
            index %= 4
            # 숫자를 갱신하는 경우
            if 0 <= x + dx[index] <= N-1 and 0 <= y + dy[index] <= N-1 and result[x + dx[index]][y + dy[index]] == 0:
                x = x + dx[index]
                y = y + dy[index]
                result[x][y] = i
                break
            else: # 갱신X, 인덱스를 벗어나거나 이미 바뀐 경우
                index += 1 #방향백터 갱신
    print(f'#{test_case}')
    for i in range(N):
        for j in range(N):
            print(result[i][j], end=' ')
        print('\n', end='')

