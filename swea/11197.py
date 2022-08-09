# 구미 3반 solving club
# 별 그리기

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    print(f'#{test_case}')
    if M == 1:
        for i in range(1, N + 1):
            print('*' * i)
    elif M == 2:
        for i in range(N, 0, -1):
            print('*' * i)
    else:
        for i in range(1, N + 1):
            print(' ' * (N - i) + '*' * (i * 2 - 1))