# 행렬찾기
import sys
sys.stdin = open('input_1258.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                temp = []
                for di, dj in [(1, 0), (0, 1)]:
                    level = 1
                    ni, nj = i + di, j + dj
                    while 0 <= ni < N and 0 <= nj < N and arr[ni][nj] != 0:
                        level += 1
                        ni, nj = i + di * level, j + dj * level
                    temp.append(level)
                result.append(temp)
                for k in range(temp[0]):
                    for l in range(temp[1]):
                        arr[i + k][j + l] = 0
    result.sort(key=lambda x: (x[0] * x[1], x[0]))
    print(f'#{tc} {len(result)}', end=' ')
    for p in result:
        print(*p, end=' ')
    print('\n', end='')
