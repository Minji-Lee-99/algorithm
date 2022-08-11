# sum

import sys
sys.stdin = open("input_14913.txt", "r")

for _ in range(1, 11):
    tc = input()
    arr = [list(map(int, input().split())) for _ in range(100)]
    result = 0
    # 가로
    for i in range(100):
        temp = 0
        for j in range(100):
            temp += arr[i][j]
        if temp > result:
            result = temp

    # 세로
    for i in range(100):
        temp = 0
        for j in range(100):
            temp += arr[j][i]
        if temp > result:
            result = temp

    # 대각선1
    temp = 0
    for i in range(100):
        temp += arr[i][i]
    if temp > result:
        result = temp

    # 대각선 2
    temp = 0
    for i in range(100):
        temp += arr[99-i][i]
    if temp > result:
        result = temp

    print(f'#{tc} {result}')

