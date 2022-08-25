# 경비원

w, h = map(int, input().split())
n = int(input())
p = [list(map(int, input().split())) for _ in range(n)]
d, num = map(int, input().split())
# (0, 0)에서 시계방향으로 경비원이 얼마나 떨어져있는지
if d == 1:
    distance = num
elif d == 4:
    distance = num + w
elif d == 2:
    distance = (w - num) + w + h
else:
    distance = (h - num) + w + h + w
ans = 0
for i in range(n):
    # 목표 지점이 시계방향으로 얼마나 떨어져있는지 계산
    if p[i][0] == 1:
        distance_p = p[i][1]
    elif p[i][0] == 4:
        distance_p = p[i][1] + w
    elif p[i][0] == 2:
        distance_p = (w - p[i][1]) + w + h
    else:
        distance_p = (h - p[i][1]) + w + h + w
    # 두쪽 방향으로 가는 것중에 어떤 것이 더 큰지 계산
    ans += min(abs(distance - distance_p), 2 * (w + h) - abs(distance - distance_p))
print(ans)


# for i in range(n):
#     # 같은 변에 있는 경우
#     if d == p[i][0]:
#         ans += abs(num - p[i][1])
#     # 위아래에 있는 경우
#     elif (d == 1 and p[i][0] == 2) or (d == 2 and p[i][0] == 1):
#         ans += (min(num + p[i][1], 2 * w - num - p[i][1]) + h)
#     # 좌우에 있는 경우
#     elif (d == 3 and p[i][0] == 4) or (d == 4 and p[i][0] == 3):
#         ans += (min(num + p[i][1], 2 * h - num + p[i][1]) + w)
#     # 하나는 위 혹은 아래, 하나는 좌 혹은 우에 있는 경우
#     elif (d == 1 and p[i][0] == 3) or (d == 3 and p[i][0] == 1):
#         ans += (num + p[i][1])
#     elif d == 1 and p[i][0] == 4:
#         ans += (w - num + p[i][1])
#     elif d == 4 and p[i][0] == 1:
#         ans = (num + w - p[i][1])
#     elif d == 2 and p[i][0] == 3:
#         ans += (num + h - p[i][1])
#     elif d == 3 and p[i][0] == 2:
#         ans += (p[i][1] + h - num)
#     elif d == 2 and p[i][0] == 4:
#         ans += (w - num + h - p[i][1])
#     else:
#         ans += (h - num + w - p[i][1])
# print(ans)

