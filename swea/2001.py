# 파리 퇴치

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_sum = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            temp = 0
            for k in range(M):
                for l in range(M):
                    temp += arr[i + k][j + l]
            if temp > max_sum:
                max_sum = temp
    print(f'#{tc} {max_sum}')


# T = int(input())
# for test_case in range(1, T + 1):
#     N, M = map(int, input().split())
#     N_lst = []
#     max_num = 0
#     # 주어진 숫자를 리스트 형식으로 만들기
#     for i in range(N):
#         N_lst.append(list(map(int, input().split())))
#     #각 인덱스별로 값을 판단
#     for i in range(N - (M-1)):
#         for j in range(N - (M - 1)):
#             num = 0
#             for k in range(M):
#                 for L in range(M):
#                     num += N_lst[i+k][j+L]
#             if num > max_num:
#                 max_num = num
#     print(f'#{test_case} {max_num}')
