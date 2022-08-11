# 색칠하기

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    orders = [list(map(int, input().split())) for _ in range(N)]
    color = [2, 1]
    arr = [[0] * 10 for _ in range(10)]
    cnt = 0
    for order in orders:
        # 주어진 영역 하나씩 불러오기
        for i in range(order[0], order[2] + 1):
            for j in range(order[1], order[3] + 1):
                # 만약 불러온 영역에 다른 색이 있으면 카운트하기
                if arr[i][j] == color[order[4] - 1]:
                    cnt += 1
                    arr[i][j] = 3 # 보라색인 경우 아예 3으로 표기하여 중복으로 카운트 되는 경우가 없도록
                else:# 겹치는 경우가 아니면 주어진 색으로 입력
                    arr[i][j] = order[4]
    print(f'#{test_case} {cnt}')
