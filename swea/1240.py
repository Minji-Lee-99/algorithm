# 단순 2진 암호코드
T = int(input())
for tc in range(1, T + 1):
    # 세로 가로
    N, M = map(int, input().split())
    arr = [list(map(int, input())) for _ in range(N)]
    x, y = 0, 0
    code = [[0, 0, 0, 1, 1, 0, 1],
            [0, 0, 1, 1, 0, 0, 1],
            [0, 0, 1, 0, 0, 1, 1],
            [0, 1, 1, 1, 1, 0, 1],
            [0, 1, 0, 0, 0, 1, 1],
            [0, 1, 1, 0, 0, 0, 1],
            [0, 1, 0, 1, 1, 1, 1],
            [0, 1, 1, 1, 0, 1, 1],
            [0, 1, 1, 0, 1, 1, 1],
            [0, 0, 0, 1, 0, 1, 1]]
    num = []
    flag = True
    # 마지막으로 1로 끝나는 위치 찾기
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                x, y = i, j
    # 암호 코드 찾아서 넣기
    for i in range(y, y - 51, -7):
        temp = arr[x][i-6:i+1]
        for j in range(10):
            if code[j] == temp:
                num.append(j)
                break
        else:
            flag = False
            break
    # 암호코드 확인
    if flag:
        even_sum = 0
        odd_sum = 0
        for i in range(0, 8, 2):
            even_sum += num[i]
        for j in range(1, 8, 2):
            odd_sum += num[j]
        if (even_sum + odd_sum * 3) % 10 == 0:
            ans = even_sum + odd_sum
        else:
            ans = 0
    else:
        ans = 0
    print(f'#{tc} {ans}')


