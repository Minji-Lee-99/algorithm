# 연산자 끼워넣기
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
                if ans < 0 or operand[k + 1] < 0:
                    a = -1 * (abs(ans) // abs(operand[k + 1]))
                else:
                    a = ans // operand[k + 1]
            perm(n, k + 1, a)
            operator[i] += 1


N = int(input())
operand = list(map(int, input().split()))
operator = list(map(int, input().split()))  # 0: 덧셈, 1: 뺄셈, 2: 곱셈, 3: 나눗셈
max_result = -10000000001
min_result = 10000000001

perm(N - 1, 0, operand[0])

print(max_result)
print(min_result)
