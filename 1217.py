# 거듭제곱
def power(N, M):
    if M == 0:
        return 1
    return N * power(N, M - 1)

for i in range(10):
    test_case = input()
    N, M = map(int, input().split())
    print(f'#{test_case} {power(N, M)}')