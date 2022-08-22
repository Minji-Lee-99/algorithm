# 빙고
N = 5
arr = [list(map(int, input().split())) for _ in range(N)]
call = []
for _ in range(N):
    call += list(map(int, input().split()))

row = [0] * 5
col = [0] * 5
dia = [0] * 2

# 가로 줄 세로줄의 합 계산하기
for i in range(N):
    for j in range(N):
        row[i] += arr[i][j]
        col[j] += arr[i][j]

# 대각선 줄의 합 계산하기
for i in range(N):
    dia[0] += arr[i][i]
    dia[1] += arr[i][N - 1 - i]

for i in range(N ** 2):
    k = l = 0
    while k < N and l < N:
        # 사회자가 부르는 수 빙고판에서 찾기
        if arr[k][l] == call[i]:
            # 찾아서 각 합에서 빼주기
            row[k] -= arr[k][l]
            col[l] -= arr[k][l]
            if k == l:
                dia[0] -= arr[k][l]
            if N - 1 - k == l:
                dia[1] -= arr[k][l]
            arr[k][l] = 0
            break
        l = l + 1
        k += l // 5
        l %= 5
    # 만약 합이 0이 된 개수가 3개 이상이라면 반복문 종료
    if row.count(0) + col.count(0) + dia.count(0) >= 3:
        break
print(i + 1)
















# def check_bingo():
#     cnt = 0
#     for i in range(N):
#         # 가로
#         j = 0
#         while j < N and arr[i][j] < 0:
#             j += 1
#         if j == N:
#             cnt += 1
#         # 세로
#         j = 0
#         while j < N and arr[j][i] < 0:
#             j += 1
#         if j == N:
#             cnt += 1
#     # 우하향 대각선
#     i = 0
#     while i < N and arr[i][i] < 0:
#         i += 1
#     if i == N:
#         cnt += 1
#     # 좌상향 대각선
#     i = 0
#     while i < N and arr[i][N - 1 - i] < 0:
#         i += 1
#     if i == N:
#         cnt += 1
#     if cnt >= 3:
#         return 1
#     return 0
#
#
# N = 5
# arr = [list(map(int, input().split())) for _ in range(N)]
# call = []
# for _ in range(N):
#     call += list(map(int, input().split()))
#
# for i in range(N ** 2):
#     # arr에서 사회자가 부른 수는 음수로 변경
#     k = l = 0
#     while k < N and l < N:
#         if arr[k][l] == call[i]:
#             arr[k][l] = -1
#             break
#         l = l + 1
#         k += l // 5
#         l %= 5
#     if i > 10:
#         if check_bingo():
#             break
# print(i + 1)
