def perm(n, k, ans):
    global max_result, min_result
    if n == k:
        if ans > max_result:
            max_result = ans
        if ans < min_result:
            min_result = ans
        return
    for i in range(4):  # 연산자 선택
        if operator[i]:
            operator[i] -= 1
            if i == 0:
                a = ans + operand[k + 1]
            elif i == 1:
                a = ans - operand[k + 1]
            elif i == 2:
                a = ans * operand[k + 1]
            else:
                a = int(ans / operand[k + 1])
            perm(n, k + 1, a)
            operator[i] += 1


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    operator = list(map(int, input().split()))  # 0: 덧셈, 1: 뺄셈, 2: 곱셈, 3: 나눗셈
    operand = list(map(int, input().split()))
    max_result = -10000000001
    min_result = 10000000001
    perm(N - 1, 0, operand[0])
    print(f'#{tc} {max_result - min_result}')

