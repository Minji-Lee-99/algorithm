orders = [list(map(int, input().split())) for _ in range(4)]
arr = [[0] * 100 for _ in range(100)]

cnt = 0
for order in orders:
    for i in range(order[0], order[2]):
        for j in range(order[1], order[3]):
            if arr[i][j] == 0:
                arr[i][j] = 1
                cnt += 1
print(cnt)