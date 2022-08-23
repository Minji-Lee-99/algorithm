k = int(input())
d = [0] * 6
v = [0] * 6
for i in range(6):
    a, b = map(int, input().split())
    d[i] = a
    v[i] = b

# 밭 전체의 크기
w = 0
h = 0
for i in range(6):
    # 세로인 것 중에서 가장 큰 것
    if (d[i] == 2 or d[i] == 1) and h < v[i]:
        h = v[i]
    # 가로인 것 중에서 가장 큰 것
    if (d[i] == 4 or d[i] == 3) and w < v[i]:
        w = v[i]

# 작은 사각형 크기
for i in range(3, -3, -1):
    # 방향이 반복되는 경우 찾기
    if d[i] == d[i - 2] and d[i - 1] == d[i - 3]:
        # 방향이 반복되는 것 중 중앙 2개의 값이 작은 사각형의 가로 세로
        print(w * h * k - v[i - 1] * v[i - 2] * k)
        break

