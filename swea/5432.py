# 쇠막대기 자르기

T = int(input())
for tc in range(1, T + 1):
    text = input()
    stack = []
    total = i = 0
    while i < len(text):
        if text[i: i+2] == '()':
            stack.append(1)
            i += 1
        elif text[i] == '(':
            stack.append('(')
        else:
            n = stack.pop()
            temp = 0
            while n != '(':
                temp += n
                n = stack.pop()
            stack.append(temp)
            total += (temp + 1)
        i += 1
    print(f'#{tc} {total}')

