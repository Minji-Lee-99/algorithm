# String

import sys
sys.stdin = open("input_1213.txt", "r", encoding = 'utf-8')

for _ in range(1, 11):
    tc = input()
    tg = input()
    st = input()
    cnt = 0
    M = len(tg)
    N = len(st)
    for i in range(N - M + 1):
        for j in range(M):
            if st[i+j] != tg[j]:
                break
        else:
            cnt += 1
    print(f'#{tc} {cnt}')



# for _ in range(1, 11):
#     tc = input()
#     tg = input()
#     st = input()
#     cnt = 0
#     for i in range(len(st)-len(tg) + 1):
#         if st[i:i + len(tg)] == tg:
#             cnt += 1
#     print(f'#{tc} {cnt}')