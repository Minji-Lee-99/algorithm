# 스도쿠 검증

T = int(input())
for test_case in range(1, T + 1):
    sudocu = []
    for i in range(9):
        sudocu.append(map(int, input().split()))
    for j in range(9):
        