# 쉬운 거스름돈

T = int(input())
for test_case in range(1, T + 1):
    money = int(input())
    units = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    print(f'#{test_case}')
    for unit in units:
        print(money // unit, end=' ')
        money %= unit
    print('\n', end='')