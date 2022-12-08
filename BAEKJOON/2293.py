# 동전1
# DP사용하기
# 1, 2, 5의 가치가 주어진 동전이 3개가 주어졌을 때, 10을 만들 수 있는 경우의 수는?
n, k = map(int, input().split())
num = []
for i in range(n):
    num.append(int(input()))
dp = [1] + [0] * k

for i in num:
    for j in range(1, k + 1):
        if j - i >= 0:
            dp[j] += dp[j - i]
    print(dp)
print(dp[k])


# 순열을 사용한 경우, 시간초과
# def perm(d, total):
#     global cnt
#     if total > k:
#         return
#     if d == n - 1:
#         temp = (k - total) // num[d]
#         if k == total + temp * num[d]:
#             cnt += 1
#         return
#     max_cnt = (k - total) // num[d] + 1
#     for i in range(max_cnt):
#         perm(d + 1, total + num[d] * i)
#
#
# n, k = map(int, input().split())
# num = []
# for i in range(n):
#     num.append(int(input()))
# cnt = 0
# num.sort(reverse=True)
# perm(0, 0)
# print(cnt)
