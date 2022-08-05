# 암호문 3

T = 10
for test_case in range(1, T + 1):
    N = int(input())
    pw = list(map(int, input().split()))
    M = int(input())
    order = input().split()
    order = order[::-1]
    index = 0
    for i in range(M):
        od = order.pop()
        if  od == 'I':
            x = int(order.pop())
            temp = []
            for j in range(int(order.pop())):
                temp.append(order.pop())
            pw = pw[:x] + temp + pw[x:]
        elif od == 'D':
            x = int(order.pop())
            pw = pw[:x] + pw[x+4:]
        elif od == 'A':
            for j in range(int(order.pop())):
                pw.append(order.pop())
    print(f'#{test_case}', end=' ')
    for i in range(10):
        print(pw[i], end=' ')
    print('\n')