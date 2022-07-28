# 준환이의 운동관리
T = int(input())
for test_case in range(1, T + 1):
    L, U, X = map(int, input().split())
    if X < L:
        print(f'#{test_case} {L - X}')
    elif X > U:
        print(f'#{test_case} -1')
    else:
        print(f'#{test_case} 0')