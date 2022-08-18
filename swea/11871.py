# 반복문자 지우기

T = int(input())
for tc in range(1, T + 1):
    text = input()
    stack = []
    for char in text: # 문자 하나씩 가지고 오기
        if stack: # 스택에 문자가 있으면
            if stack[-1] == char: # 제일 마지막 문자가 넣으려는 문자와 같은지 확인
                stack.pop() # 같으면 같은 문자 제거
            else: # 다르면 넣기
                stack.append(char)
        else: # 스택에 문자가 없으면 무조건 넣기
            stack.append(char)
    print(f"#{tc} {len(stack)}")
