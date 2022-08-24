# 개미

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())
reverse = [0, -1, 1]
dp, dq = 1, 1







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


