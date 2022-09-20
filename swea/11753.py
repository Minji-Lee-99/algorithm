# 이진수2

T = int(input())
for tc in range(1, 1 + T):
    num = float(input())
    ans = ''
    flag = False
    for i in range(12):
        num *= 2
        if num >= 1:
            num -= 1
            ans += '1'
            if num == 0:
                flag = True
                break
        else:
            ans += '0'
    if not flag:
        ans = 'overflow'
    print(f'#{tc} {ans}')
