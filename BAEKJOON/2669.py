orders = [list(map(int, input().split())) for _ in range(4)]    # 직사각형 면적
arr = [[0] * 100 for _ in range(100)]   # 좌표 평면

cnt = 0
for order in orders:   # 직사각형 하나하나 가지고 오기
    for i in range(order[0], order[2]):    # 넓이에 해당하는 좌표 하나씩 가지고 오기
        for j in range(order[1], order[3]):
            if arr[i][j] == 0:   # 해당 좌표가 0이면 1로 표시하고 개수 세기
                arr[i][j] = 1
                cnt += 1
print(cnt)
