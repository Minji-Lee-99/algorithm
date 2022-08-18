# 줄 세우기

N = int(input())
arr = list(map(int, input().split()))   # 뽑은 숫자
std = list(range(1, N + 1))    # 학생 번호 리스트

for i in range(1, N):   # 자리를 옮길 학생 번호
    for j in range(arr[i]):   # 학생이 뽑은 번호만큼 한자리씩 앞으로 이동
        std[i - j], std[i - j - 1] = std[i - j - 1], std[i - j]

# 결과 출력
print(*std)
