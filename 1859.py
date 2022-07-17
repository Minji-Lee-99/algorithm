#백만장자프로젝트
#22.05.04

def count_max(num, price):
    Flag = True
    total = 0
    while (Flag):
        max_price = 0
        max_index = 0
        sub_total = 0
        for i in range(len(price)):
            if price[i] >= max_price:
                max_price = price[i]
                max_index = i
        sub_total = price[max_index] * max_index
        sub_total -= sum(price[:max_index])
        total += sub_total
        price = price[(max_index + 1):]
        if len(price) <= 1:
            Flag = False
    return total


T = int(input())
for test_case in range(1, T + 1):
    num = int(input())
    price = list(map(int, input().split()))
    total = count_max(num, price)
    # 출력
    print('#%d %d' % (test_case, total))

