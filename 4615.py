# 재밌는 오셀로 게임

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split()) # N: 보드의 길이 M: 돌을 놓는 횟수
    # 초기 보드 세팅
    board = [[0 for i in range(N)] for j in range(N)]
    board[N // 2][N // 2] = board[(N // 2) - 1][(N // 2) - 1] = 2
    board[N // 2][(N // 2) - 1] = board[(N // 2) - 1][N // 2] = 1
    # 방향 벡터 설정
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [-1, -1, 0, 1, 1, 1, 0, -1]
    colors = [0, 2, 1] # 반대 색을 참조할 수 있는 리스트
    result = [0, 2, 2] # 돌 개수 저장할 리스트
    for i in range(M): # 돌을 놓는 횟수 만큼 반복
        y, x, color = map(int, input().split()) # 어떤 위치에 어떤 돌을 놓을 것인지
        board[x - 1][y - 1] = color # 입력된 위치에 돌을 놓고, 개수 카운트
        result[color] += 1
        for j in range(len(dx)): # 8방향으로 탐색
            level = 1 # 방향으로 몇번 들어갔는지 나타내는 변수
            change_list = [] # 변경되어야 하는 좌표 담는 리스트
            while 1:
                new_x = -1 + x + dx[j] * level
                new_y = -1 + y + dy[j] * level
                # 인덱스가 벗어나면 다른 돌을 뒤집을 수 있는 경우가 아니므로, 리스트를 비우고 반복문 탈출
                if new_x < 0 or new_x > N - 1 or new_y < 0 or new_y > N - 1:
                    change_list.clear()
                    break
                # 반대 돌을 만난 경우로 이 경우엔 바꿔야 하는 리스트에 담고 그 다음 위치를 확인
                elif board[new_x][new_y] == colors[color]:
                    change_list.append((new_x, new_y))
                    level += 1
                # 어떤 돌도 놓여있지 않은 경우로, 다른 돌을 뒤집을 수 있는 경우가 아니므로, 리스트를 비우고 반복문 탈출
                elif board[new_x][new_y] == 0:
                    change_list.clear()
                    break
                else: # 같은 색의 돌을 만난 경우로, 반복문을 종료한다.
                    break
            # change_list에 들어있는 좌표를 통해 개수를 갱신하고 보드를 갱신한다. 
            result[color] += len(change_list)
            result[colors[color]] -= len(change_list)
            for point in change_list:
                board[point[0]][point[1]] = color
    print(f'#{test_case} {result[1]} {result[2]}')
