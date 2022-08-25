# 피자 굽기
T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    amt = list(map(int, input().split()))
    board = amt[0:n]
    idx = list(range(0, n))
    s = 0
    i = n
    while 1:
        board[s] //= 2
        if board[s] == 0 and i < m:
            board[s] = amt[i]
            idx[s] = i
            i += 1
        if sum(board) == 0:
            break
        s = (s + 1) % n
    print(f'#{tc} {idx[s] + 1}')





# T = int(input())
# for tc in range(1, T + 1):
#     n, m = map(int, input().split())
#     amt = list(map(int, input().split()))
#     idx = list(range(0, n))    # 마지막에 인덱스 값을 확인하기 위한 배열
#     bake = [100] * n    # 몇 바퀴가 지나면 피자를 꺼낼 수 있는지 저장하는 배열
#     fo = n - 1
#     for i in range(n):
#         # 로그를 통해서 몇바퀴가 지나면 꺼낼 수 있는지 계산 및 가장 작은 값 찾기(단, 가장 작은 값이 0은 안됨)
#         bake[i] = (int(math.log2(amt[i])) + 1)
#         if bake[i] < bake[fo] and bake[i]:
#             fo = i
#     i = n
#     while 1:
#         flag = True
#         for j in range(n):
#             bake[j] -= bake[fo]   # 가장 작은 값만큼 빼기
#             if bake[j] == 0 and i < m:    # 빠진 피자가 있으면 새거 넣기
#                 bake[j] = int(math.log2(amt[i])) + 1
#                 idx[j] = i
#                 i += 1
#             if bake[j] != 0 and bake[j] != 1:   # 피자가 다 빠져 나갔는지 확인
#                 flag = False
#         if flag:
#             break
#         for j in range(n):  # 다시 가장 작은 값 찾기
#             if bake[fo] > bake[j] and bake[j]:
#                 fo = j
#     ans = 0
#     for i in range(n):
#         if bake[i] == 1:
#             ans = i
#     print(f'#{tc} {idx[ans] + 1}')

