# 간단한 소인수분해
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    print(f'#{tc}', end=' ')
    for num in [2, 3, 5, 7, 11]:
        cnt = 0
        while N % num == 0:
            N //= num
            cnt += 1
        print(cnt, end=' ')
    print('\n', end='')





# T = int(input())
# for test_case in range(1, T + 1):
#     number = int(input())
#     print(f'#{test_case}', end=' ')
#     for num in [2, 3, 5, 7, 11]:
#         count = 0
#         while(number % num == 0):
#             number //= num
#             count += 1
#         print(count, end=' ')
#     print('\n', end='')