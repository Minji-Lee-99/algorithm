# 계산기3

for tc in range(1, 11):
    N = int(input())
    formula = input()
    stack = []
    post_formula = []
    isp = {'(': 0, '*': 2, '+': 1}
    icp = {'(': 3, '*': 2, '+': 1}
    i = 0
    while i < N:
        # 숫자
        if formula[i].isdecimal():
            post_formula.append(formula[i])
        # 연산자
        else:
            # 닫는 괄호
            if formula[i] == ')':
                n = stack[-1]
                while n != '(':    # 여는 괄호를 만날 때까지 pop 반복
                    post_formula.append(stack.pop())
                    n = stack[-1]
                stack.pop()    # 여는 괄호 삭제
            # 이외의 연산자
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
                else:
                    # 스택이 비어있으면 삽입
                    stack.append(formula[i])
        i += 1
    # 스택에 남은 부분 모두 pop해주기
    while stack:
        post_formula.append(stack.pop())
    # 계산하기
    stack = []
    for n in post_formula:
        if n.isdecimal():
            stack.append(int(n))
        else:
            op2 = stack.pop()
            op1 = stack.pop()
            if n == '*':
                stack.append(op1 * op2)
            elif n == '+':
                stack.append(op1 + op2)
    print(f'#{tc} {stack[0]}')




