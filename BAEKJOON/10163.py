# 색종이
N = int(input())
arr = [[0] * 1001 for _ in range(1001)]

# 입력받은 사각형 체크
for k in range(1, N + 1):
    x, y, w, h = map(int, input().split())
    for i in range(y, y + h):
        for j in range(x, x + w):
            arr[i][j] = k

# 개수 체크
results = [0] * (N + 1)
for i in range(1001):
    for j in range(1001):
        results[arr[i][j]] += 1

# 출력
for idx in range(1, N + 1):
    print(results[idx])


# # 입력받은 사각형 체크
# for k in range(1, N + 1):
#     x, y, w, h = map(int, input().split())
#     for i in range(y, y + h):
#         arr[i][x:x+w] = [k] * w
#
# # 개수 체크
# results = [0] * (N + 1)
# for i in range(1001):
#     for j in range(1001):
#         results[arr[i][j]] += 1
#
# # 출력
# for idx in range(1, N + 1):
#     print(results[idx])