# 방배정
import math

N, K = map(int, input().split())
students = {}
result = 0

# 학생 수 입력 받으면서 개수 세기
for _ in range(N):
    s, y = input().split()
    if (s, y) in students:  # (성별, 학년)을 key로 하는 딕셔너리로 명수 세기
        students[(s, y)] += 1
    else:
        students[(s, y)] = 1

# 성별, 학생에 따라서 방 개수 계산해주기/ 명수를 정원으로 나누되, 소수점은 올림
for key in students:
    result += math.ceil(students[key] / K)

print(result)

