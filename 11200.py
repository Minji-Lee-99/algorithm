T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    print(f'#{test_case}')
    mid = N // 2
    if M == 1:
        for i in range(1, mid + 2):
            print('*' * i)
        for i in range(mid, 0, -1):
            print('*' * i)
    elif M == 2:
        for i in range(1, mid + 2):
            print(' ' * (mid + 1 - i) + '*' * i)
        for i in range(mid, 0, -1):
            print(' ' * (mid + 1 - i) + '*' * i)
    elif M == 3:
        for i in range(mid + 1, 0, -1):
            print(' ' * (mid - i + 1) + '*' * (2 * i - 1))
        for i in range(2, mid + 2):
            print(' ' * (mid - i + 1) + '*' * (2 * i - 1))
    else:
        for i in range(mid + 1, 0, -1):
            print(' ' * (mid + 1 - i) + '*' * i)
        for i in range(2, mid + 2):
            print(' ' * mid + '*' * i)