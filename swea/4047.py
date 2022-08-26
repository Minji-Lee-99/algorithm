# 영준이의 카드 카운팅

T = int(input())
for tc in range(1, T + 1):
    t = input()
    card = {}
    flag = True
    for i in range(0, len(t), 3):
        if t[i:i+3] in card:
            flag = False
            break
        else:
            card[t[i:i+3]] = 1
    if flag:
        s = d = h = c = 13
        for key in card:
            if key[0] == 'S':
                s -= 1
            elif key[0] == 'D':
                d -= 1
            elif key[0] == 'H':
                h -= 1
            elif key[0] == 'C':
                c -= 1
        print(f'#{tc} {s} {d} {h} {c}')
    else:
        print(f'#{tc} ERROR')

























# T = int(input())
# for tc in range(1, T + 1):
#     card = input()
#     S = [0] * 14
#     D = [0] * 14
#     H = [0] * 14
#     C = [0] * 14
#     i = 0
#     flag = True
#     while i < len(card):
#         if card[i] == 'S':
#             num = int(card[i+1: i+3])
#             if S[num] != 0:
#                 flag = False
#                 break
#             else:
#                 S[num] += 1
#             i += 3
#         elif card[i] == 'D':
#             num = int(card[i+1: i+3])
#             if D[num] != 0:
#                 flag = False
#                 break
#             else:
#                 D[num] += 1
#             i += 3
#         elif card[i] == 'H':
#             num = int(card[i+1: i+3])
#             if H[num] != 0:
#                 flag = False
#                 break
#             else:
#                 H[num] += 1
#             i += 3
#         else:
#             num = int(card[i+1: i+3])
#             if C[num] != 0:
#                 flag = False
#                 break
#             else:
#                 C[num] += 1
#             i += 3
#     if flag:
#         print(f'#{tc} {13 - sum(S)} {13 - sum(D)} {13 - sum(H)} {13 - sum(C)}')
#     else:
#         print(f'#{tc} ERROR')