# 계산기2

for tc in range(1, 11):
    N = int(input())
    formula = input()
    stack = []
    post_formula = []
    isp = {'*': 2, '+': 1}
    icp = {'*': 2, '+': 1}
    i = 0
    # 후위표기식으로 전환
    while i < N:
        # 숫자
        if formula[i].isdecimal():
            post_formula.append(formula[i])
        # 연산자
        else:
            # 스택의 길이가 1이상인 경우
            if stack:
                n = stack[-1]
                # 토큰이 스택의 top 원소보다 우선순위가 높을 때까지 pop
                while isp[n] >= icp[formula[i]]:
                    post_formula.append(stack.pop())
                    if stack:
                        n = stack[-1]
                    else:
                        break
                stack.append(formula[i])    # 토큰을 스택에 추가
            # 스택이 비어있는 경우
            else:
                stack.append(formula[i])
        i += 1
    # 스택에 남은 부분 모두 pop해주기
    while stack:
        post_formula.append(stack.pop())

    # 계산
    for n in post_formula:
        if n.isdecimal():   # 숫자면 stack에 추가
            stack.append(int(n))
        else:   # 연산자면 스택에서 피연산자 2개 꺼내서 연산 후 다시 넣기
            op2 = stack.pop()
            op1 = stack.pop()
            if n == '*':
                stack.append(op1 * op2)
            elif n == '+':
                stack.append(op1 + op2)
    print(f'#{tc} {stack[0]}')
