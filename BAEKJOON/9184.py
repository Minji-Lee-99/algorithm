# 신나는 함수 실행

# def w(a, b, c):
#     if (a, b, c) in memo:
#         return memo[(a, b, c)]
#     if a <= 0 or b <= 0 or c <= 0:
#         ans = 1
#     elif a > 20 or b > 20 or c > 20:
#         ans = w(20, 20, 20)
#     elif a < b < c:
#         ans = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
#     else:
#         ans = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
#     memo[(a, b, c)] = ans
#     return ans
#
#
# memo = {}
# while True:
#     a, b, c = map(int, input().split())
#     if a == b == c == -1:
#         break
#     result = w(a, b, c)
#     print(f'w({a}, {b}, {c}) = {result}')


def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:  # base case
        return 1
    elif a > 20 or b > 20 or c > 20:  # 이 경우는 메모해둘 필요가 없음(어차피 20, 20, 20으로 들어올 것이기 때문)
        return w(20, 20, 20)
    elif memo[a][b][c] != 0:  # 계산한 적이 있는 값이라면 해당 값 리턴
        return memo[a][b][c]
    elif a < b < c:  # 계산한 값 메모에 저장해주기
        memo[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
        return memo[a][b][c]
    else:
        memo[a][b][c] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
        return memo[a][b][c]


memo = [[[0] * 21 for _ in range(21)] for _ in range(21)]
while True:
    a, b, c = map(int, input().split())
    if a == b == c == -1:  # 모두 -1이면 멈추기
        break
    result = w(a, b, c)
    print(f'w({a}, {b}, {c}) = {result}')
