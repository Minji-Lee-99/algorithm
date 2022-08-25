# 개미

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())
t2 = t
# 가로 좌표 계산
if t > w - p:
    t -= w - p
    rem = t % w
    quo = t // w
    if quo % 2:   # quo가 홀수이면 0에 위치하고 있는 것
        x = rem
    else:   # quo가 짝수이면 w에 위치하고 있는 것
        x = w - rem
else:   # 가로축이 벽에 한번도 안부딪히는 경우
    x = p + t

# 세로 좌표 계산
if t2 > h - q:
    t2 -= h - q
    rem = t2 % h
    quo = t2 // h
    if quo % 2:
        y = rem
    else:
        y = h - rem
else:   # 세로축이 벽에 한번도 안부딪히는 경우
    y = q + t2
print(x, y)

















# w, h = map(int, input().split())
# p, q = map(int, input().split())
# t = int(input())
# reverse = [0, -1, 1]
# dp, dq = 1, 1
# sub = [0, 0]
# while t > 0:
#     if dp > 0:
#         sub[0] = w - p
#     else:
#         sub[0] = p
#     if dq > 0:
#         sub[1] = h - q
#     else:
#         sub[1] = q
#     if sub[1] > sub[0]:
#         min_sub = 0
#     elif sub[1] == sub[0]:
#         min_sub = -1
#     else:
#         min_sub = 1
#     if t >= sub[min_sub]:
#         if dp > 0:
#             p = p + sub[min_sub]
#         else:
#             p = p - sub[min_sub]
#         if dq > 0:
#             q = q + sub[min_sub]
#         else:
#             q = q - sub[min_sub]
#         t -= sub[min_sub]
#         if min_sub == -1:
#             dq = reverse[dq]
#             dp = reverse[dp]
#         elif min_sub == 1:
#             dq = reverse[dq]
#         else:
#             dp = reverse[dp]
#     else:
#         if dp > 0:
#             p = p + t
#         else:
#             p = p - t
#         if dq > 0:
#             q = q + t
#         else:
#             q = q - t
#         t = 0
# print(p, q)


