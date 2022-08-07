# 암호문 3

T = 10
for test_case in range(1, T + 1):
    N = int(input())
    pw = list(map(int, input().split()))
    M = int(input())
    order = input().split()
    order.append(0)
    order = order[::-1]
    for i in range(M):
        od = order.pop()
        if  od == 'I':
            x = int(order.pop())
            y = int(order.pop())
            pw = pw[:x] + order[-1:len(order)-int(y)-1:-1] + pw[x:]
            order = order[:len(order)-int(y)]
        elif od == 'D':
            x = int(order.pop())
            pw = pw[:x] + pw[x+int(order.pop()):]
        elif od == 'A':
            y = int(order.pop())
            pw = pw + order[-1:len(order)-int(y)-1:-1]
            order = order[:len(order)-int(y)]
    print(f'#{test_case}', end=' ')
    for i in range(10):
        print(pw[i], end=' ')
    print('\n')


# T = 10
# for test_case in range(1, T + 1):
#     N = int(input())
#     pw = list(map(int, input().split()))
#     M = int(input())
#     order = input().split()
#     order = order[::-1]
#     index = 0
#     for i in range(M):
#         od = order.pop()
#         if  od == 'I':
#             x = int(order.pop())
#             temp = []
#             for j in range(int(order.pop())):
#                 temp.append(order.pop())
#             pw = pw[:x] + temp + pw[x:]
#         elif od == 'D':
#             x = int(order.pop())
#             pw = pw[:x] + pw[x+int(order.pop()):]
#         elif od == 'A':
#             for j in range(int(order.pop())):
#                 pw.append(order.pop())
#     print(f'#{test_case}', end=' ')
#     for i in range(10):
#         print(pw[i], end=' ')
#     print('\n')