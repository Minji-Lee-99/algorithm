# 스도쿠
def bt(n, k):
    global flag
    if n == k:
        flag = True
        return
    else:
        x, y = blank[k]
        for i in range(1, 10):
            if flag:
                return
            if not cnts_row[x][i] and not cnts_col[y][i] and not cnts_block[x // 3 * 3 + y // 3][i]:
                arr[x][y] = i
                cnts_row[x][i] = 1
                cnts_col[y][i] = 1
                cnts_block[x // 3 * 3 + y // 3][i] = 1
                bt(n, k + 1)
                cnts_row[x][i] = 0
                cnts_col[y][i] = 0
                cnts_block[x // 3 * 3 + y // 3][i] = 0


arr = [list(map(int, input().split())) for _ in range(9)]
cnts_row = [[0] * 10 for _ in range(9)]  # 각 행의 0~9숫자가 있는지 없는지 판단하는 2중리스트
cnts_col = [[0] * 10 for _ in range(9)]  # 각 열에 0~9숫자가 있는지 없는지 판단하는 리스트
cnts_block = [[0] * 10 for _ in range(9)]  # 각 사각형에 0~9숫자가 있는지 없는지 판단하는 리스트
blank = []  # 숫자가 비어있는 좌표

# i행에 0~9가 있는지 없는지 판단하는 리스트 만들기
for i in range(9):
    for j in range(9):
        if arr[i][j]:
            cnts_row[i][arr[i][j]] = 1
        else:
            blank.append([i, j])

# i열에 0~9가 있는지 없는지 판단하는 리스트 만들기
for i in range(9):
    for j in range(9):
        cnts_col[i][arr[j][i]] = 1

# i번째 사각형에 0~9가 있는지 없는지 판단하는 리스트 만들기
for i in range(9):
    for j in range(9):
        cnts_block[i // 3 * 3 + j // 3][arr[i][j]] = 1

flag = False
bt(len(blank), 0)
for i in range(9):
    print(*arr[i])
