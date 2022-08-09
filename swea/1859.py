#백만장자프로젝트
#22.05.04

# def count_max(num, price):
#     Flag = True
#     total = 0
#     while (Flag):
#         max_price = 0
#         max_index = 0
#         sub_total = 0
#         # 리스트에서 가장 큰 값 찾기
#         for i in range(len(price)):
#             if price[i] >= max_price:
#                 max_price = price[i]
#                 max_index = i
#         # 가장 큰 값 앞의 인덱스들을 모두 사서 팔기
#         sub_total = price[max_index] * max_index
#         sub_total -= sum(price[:max_index])
#         total += sub_total
#         # 리스트 갱신
#         price = price[(max_index + 1):]
#         # 리스트가 1개 이하로 남았을 때는 의미가 없기 때문에 종료
#         if len(price) <= 1:
#             Flag = False
#     return total


# T = int(input())
# for test_case in range(1, T + 1):
#     num = int(input())
#     price = list(map(int, input().split()))
#     total = count_max(num, price)
#     # 출력
#     print('#%d %d' % (test_case, total))

# 2
# 22.07.28

# 시간초과로 통과 X
# T = int(input())
# for test_case in range(1, T + 1):
#     count = int(input())
#     price = list(map(int, input().split()))
#     total = 0
#     for i in range(count):
#         max_profit = 0
#         for j in range(i+1, count):
#             if max_profit < (price[j] - price[i]):
#                 max_profit = price[j] - price[i]
#         total += max_profit
#     print(f'#{test_case} {total}')



