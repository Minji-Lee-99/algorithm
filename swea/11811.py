T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    num = int(input())
    cnt = [0] * 10
    for _ in range(N):
        cnt[num % 10] += 1
        num //= 10
    max_i, max_n = 0, cnt[0]
    for i in range(1, 10):
        if max_n <= cnt[i]:
            max_n = cnt[i]
            max_i = i
    print(f'#{test_case} {max_i} {max_n}')