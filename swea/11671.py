# 기지국

# 함수 사용 X
T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = [list(input()) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[i][j] != 'H' and arr[i][j] != 'X':
                for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                    for l in range(1, ord(arr[i][j]) - 63):
                        ni, nj = i + di * l, j + dj * l
                        if 0 <= ni < n and 0 <= ni < n and arr[ni][nj] == 'H':
                            arr[ni][nj] = 'X'
    ans = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'H':
                ans += 1
    print(f'#{tc} {ans}')



# 함수 써서 하기
# def check(ii, jj, k):
#     for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
#         for l in range(1, k + 1):
#             ni, nj = ii + di * l, jj + dj * l
#             if 0 <= ni < n and 0 <= ni < n and arr[ni][nj] == 'H':
#                 arr[ni][nj] = 'X'
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     n = int(input())
#     arr = [list(input()) for _ in range(n)]
#     for i in range(n):
#         for j in range(n):
#             if arr[i][j] == 'A':
#                 check(i, j, 1)
#             elif arr[i][j] == 'B':
#                 check(i, j, 2)
#             elif arr[i][j] == 'C':
#                 check(i, j, 3)
#     ans = 0
#     for i in range(n):
#         for j in range(n):
#             if arr[i][j] == 'H':
#                 ans += 1
#     print(f'#{tc} {ans}')
