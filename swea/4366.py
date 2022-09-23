# 정식이의 은행업무
T = int(input())
for tc in range(1, T + 1):
    num2 = input()
    num3 = input()
    pn = []
    # 3진수를 10진수로 바꾸기
    num3_to_10 = 0
    n = len(num3)
    for i in range(n - 1, -1, -1):
        num3_to_10 += (3 ** i) * int(num3[n - i - 1])
    # 3진수에서 한자리씩 바꿔가면서 가능한 경우의 수를 pn에 넣기
    for i in range(n - 1, -1, -1):
        for j in [0, 1, 2]:
            if j != int(num3[n - i - 1]):
                pn.append(num3_to_10 - (3**i) * int(num3[n - i - 1]) + (3**i) * j)
    # 2진수를 10진수로 바꾸기
    num2_to_10 = 0
    n = len(num2)
    for i in range(n - 1, -1, -1):
        num2_to_10 += (2 ** i) * int(num2[n - i - 1])
    # 2진수를 한자리씩 바꿔가며 3진수에 같은 값이 있는지 보기
    for i in range(n - 1, -1, -1):
        ans = num2_to_10 - (2**i) * int(num2[n - i - 1]) + (2**i) * abs(int(num2[n - i - 1]) - 1)
        if ans in pn:  # 있다면 멈추고 출력
            break
    print(f'#{tc} {ans}')


