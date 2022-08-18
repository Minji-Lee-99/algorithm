# 괄호 검사

def matching(text):
    stack = []
    for char in text:
        if char == '(' or char == '{':  # 여는 괄호면 stack에 넣기
            stack.append(char)
        elif char == ')' or char == '}':   # 닫는 괄호면 stack에서 하나 꺼내고 짝 확인
            if len(stack) > 0:
                n = stack.pop()
                if char == ')' and n != '(':
                    return 0
                elif char == '}' and n != '{':
                    return 0
            else:   # stack에 아무것도 없으면 짝이 안맞는 것이므로 0
                return 0
    if len(stack):   # 모든 text를 다 보았는데 stack에 무언가 남아있으면 짝이 안맞는 것
        return 0
    return 1


T = int(input())
for tc in range(1, T + 1):
    text = input()
    print(f'#{tc} {matching(text)}')
