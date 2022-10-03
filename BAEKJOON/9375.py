# 패션왕 신해빈
from itertools import combinations

# 재귀는 시간이 오래 걸림
# def powerset(n, k, ans):
#     global total
#     if n == k:
#         total += ans
#     else:
#         powerset(n, k + 1, ans * cnts[k])
#         powerset(n, k + 1, ans)

# 함수 사용해보기!
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     kinds = {}
#     # 입력받기(종류별로 개수 세기)
#     for i in range(N):
#         name, kind = input().split()
#         if kind in kinds:
#             kinds[kind] += 1
#         else:
#             kinds[kind] = 1
#     cnts = list(kinds.values())
#     result = []
#     for i in range(1, len(cnts) + 1):
#         result += list(combinations(cnts, i))
#     total = 0
#     for a in result:
#         ssum = 1
#         for n in a:
#             ssum *= n
#         total += ssum
#     print(total)


# 반복문 사용해보기!
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     kinds = {}
#     # 입력받기(종류별로 개수 세기)
#     for i in range(N):
#         name, kind = input().split()
#         if kind in kinds:
#             kinds[kind] += 1
#         else:
#             kinds[kind] = 1
#     cnts = list(kinds.values())
#     result = [1]
#     total = 0
#     for cnt in cnts:
#         size = len(result)
#         for j in range(size):
#             num = result[j] * cnt
#             result.append(num)
#             total += num
#     print(total)

# 계산
# 116ms
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    kinds = {}
    # 입력받기(종류별로 개수 세기)
    for i in range(N):
        name, kind = input().split()
        if kind in kinds:
            kinds[kind] += 1
        else:
            kinds[kind] = 1
    cnts = list(kinds.values())
    ans = 1
    for cnt in cnts:
        ans *= (cnt + 1)
    print(ans - 1)
