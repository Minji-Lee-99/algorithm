# 방배정
import math

N, K = map(int, input().split())
students = {}
result = 0

# 학생 수 입력 받으면서 개수 세기
for _ in range(N):
    s, y = input().split()
    if (s, y) in students:
        students[(s, y)] += 1
    else:
        students[(s, y)] = 1

# 성별, 학생에 따라서 방 개수 계산해주기
for key in students:
    result += math.ceil(students[key] / K)

print(result)

