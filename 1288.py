# 새로운 불면증 치료법

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    number = set()
    count = 1
    while 1:
        number.update(set(str(N * count)))
        if len(number) == 10:
            print(f'#{test_case} {count * N}')
            break
        count += 1
