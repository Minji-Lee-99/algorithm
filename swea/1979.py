#어디에 단어가 들어갈 수 있을까

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    # 가로 찾기
    for i in range(N):
        j = 0
        while j < N:
            temp = 0
            while j < N and arr[i][j]:
                temp += 1
                j += 1
            if temp == K:
                cnt += 1
            j += 1
    # 세로 찾기
    for i in range(N):
        j = 0
        while j < N:
            temp = 0
            while j < N and arr[j][i]:
                temp += 1
                j += 1
            if temp == K:
                cnt += 1
            j += 1
    print(f'#{tc} {cnt}')








# T = int(input())
# for test_case in range(1, T + 1):
#     # 입력
#     N, K = map(int, input().split())
#     N_lst = []
#     for i in range(N):
#         N_lst.append(list(map(int, input().split())))
#     count = 0 # 가능한 위치 개수 세는 변수
#     # 가로 방향에 가능한 위치 탐색
#     for k in range(N):
#         length = 0
#         for l in range(N):
#             if N_lst[k][l] == 1:
#                 length += 1
#                 if l == N - 1 and length == K:
#                     count += 1
#             else:
#                 if length == K:
#                     count += 1
#                 length = 0
#     # 세로 방향에 가능한 위치 탐색
#     for i in range(N):
#         length = 0
#         for j in range(N):
#             if N_lst[j][i] == 1:
#                 length += 1
#                 if j == N - 1 and length == K:
#                     count += 1
#             else:
#                 if length == K:
#                     count += 1
#                 length = 0
#     print(f'#{test_case} {count}')