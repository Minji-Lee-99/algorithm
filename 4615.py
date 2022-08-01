# 재밌는 오셀로 게임

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    board = [[0 for i in range(N)] for j in range(N)]
    board[N // 2][N // 2] = board[(N // 2) - 1][(N // 2) - 1] = 2
    board[N // 2][(N // 2) - 1] = board[(N // 2) - 1][N // 2] = 1
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [-1, -1, 0, 1, 1, 1, 0, -1]
    colors = [0, 2, 1]
    result = [0, 2, 2]
    for i in range(M):
        y, x, color = map(int, input().split())
        # print('color = ', color)
        board[x - 1][y - 1] = color
        result[color] += 1
        # 탐색
        for j in range(len(dx)):
            level = 1
            change_list = []
            while 1:
                try:
                    print('check:', x - 1  + dx[j] * level,y-1 + dy[j] * level, colors[color])
                    if board[-1 + x + dx[j] * level][-1 + y + dy[j] * level] == colors[color]:
                        change_list.append((x - 1 + dx[j] * level, y - 1 + dy[j] * level))
                        level += 1
                        print('here:', change_list)
                    elif board[-1 + x + dx[j] * level][y - 1 + dy[j] * level] == 0:
                        change_list.clear()
                        break
                    else:
                        break
                except IndexError:
                    change_list.clear()
                    break
            result[color] += len(change_list)
            result[colors[color]] -= len(change_list)
            for point in change_list:
                board[point[0]][point[1]] = color
            print(board)
    print(f'#{test_case} {result[1]} {result[2]}')
