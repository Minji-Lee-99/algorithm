# 네방향 탐색



T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    N_lst = [list(map(int, input().split())) for _ in range(N)]
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    result = 0
    for i in range(N):
        for j in range(N):
            for idx in range(4):
                nx = i + dx[idx]
                ny = j + dy[idx]
                if 0 <= nx < N and 0 <= ny < N:
                    num = N_lst[i][j] - N_lst[nx][ny]
                    result += (-1) * num if num < 0 else num
    print(f'#{test_case} {result}')
