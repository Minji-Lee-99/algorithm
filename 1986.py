T = int(input())
for test_case in range(1, T + 1):
    num = int(input())
    total = 0
    for i in range(1, num + 1):
        if i % 2:
            total += i
        else:
            total -= i
    print(f'#{test_case} {total}')
    