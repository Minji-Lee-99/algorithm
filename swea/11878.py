# 계산기

T = int(input())

for tc in range(1, T + 1):
    formula = input().split()
    stack = []
    for n in formula:
        if n.isdecimal():
            stack.append(int(n))
        else:
            if n == '.':
                result = stack.pop() if stack else 'error'
            else:
                if len(stack) > 1:
                    op2 = stack.pop()
                    op1 = stack.pop()
                    if n == '+':
                        stack.append(op1 + op2)
                    elif n == '-':
                        stack.append(op1 - op2)
                    elif n == '*':
                        stack.append(op1 * op2)
                    else:
                        stack.append(op1 // op2)
                else:
                    result = 'error'
                    break
    if stack:
        result = 'error'
    print(f'#{tc} {result}')
