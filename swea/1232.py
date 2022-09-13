# 사칙연산
def postorder(n):
    if num[n] != 0:
        return num[n]
    else:
        l = postorder(ch1[n])
        r = postorder(ch2[n])
        op = oper[n]
        if op == "+":
            return l + r
        elif op == "-":
            return l - r
        elif op == "*":
            return l * r
        else:
            return l / r


for tc in range(1, 11):
    V = int(input())
    ch1 = [0] * (V + 1)
    ch2 = [0] * (V + 1)
    oper = [""] * (V + 1)
    num = [0] * (V + 1)
    for i in range(V):
        lst = input().split()
        if len(lst) == 2:
            num[int(lst[0])] = int(lst[1])
        else:
            oper[int(lst[0])] = lst[1]
            ch1[int(lst[0])] = int(lst[2])
            ch2[int(lst[0])] = int(lst[3])
    print(f'#{tc} {int(postorder(1))}')

