# 23시간

T = int(input())
for test_case in range(1, T + 1):
    print(f'#{test_case} {(sum(map(int, input().split()))) % 24}')
