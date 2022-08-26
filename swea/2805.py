# 농작물 수확하기

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, list(input()))) for _ in range(N)]
    ans = 0
    mid = N // 2
    for i in range(0, mid + 1):
        for j in range(mid - i, mid + i + 1):
            ans += arr[i][j]
    for k in range(0, mid):
        for l in range(k + 1, N - k - 1):
            ans += arr[mid + k + 1][l]
    print(f'#{tc} {ans}')


# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = [list(map(int, list(input()))) for _ in range(N)]
#     total = 0
#     mid = N // 2
#     for i in range(mid):
#         for j in range(mid - i, N - mid + i): # 중간에서 얼마나 떨어졌는지는 mid - i를 통해서 구함
#             total += arr[i][j]
#     for i in range(mid, N):
#         for j in range(i - mid, N - i + mid):
#             total += arr[i][j]
#     print(f'#{tc} {total}')
