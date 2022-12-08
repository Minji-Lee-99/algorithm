# 리모컨
# 모든 경우의 수를 다 보는 brute force로 문제 해결

def bf(num):
    global result
    for n in button:
        num1 = num
        num1 += str(n)
        temp = len(num1) + abs(int(target) - int(num1))
        if temp < result:
            result = temp
        if len(num1) < 6:
            bf(num1)


target = input()
M = int(input())
button = {i for i in range(10)}
if M:
    broken = set(map(int, input().split()))
else:
    broken = set()
button = button - broken

result = abs(100 - int(target))
if result:  # 원하는 채널이 100이면 움직이지 않아도 되기 때문에
    bf('')
print(result)





# target = input()
# M = int(input())
# if M:
#     broken = list(map(int, input().split()))
# else:
#     broken = []
# button_tf = [True for i in range(10)]  # 버튼이 고장났는지 아닌지를 나타냄
# for b in broken:
#     button_tf[b] = False
#
# # 가장 작은 버튼과 가장 큰 숫자 버튼 저장
# min_button = 10
# max_button = 0
# for i in range(10):
#     if button_tf[i] and i < min_button:
#         min_button = i
#     if button_tf[i] and i > max_button:
#         max_button = i
#
# number = ''
# idx = 0
# while len(number) < len(target):
#     if int(target) == 100:  # 원하는 채널이 100이면 더 볼 필요가 없음.
#         print(0)
#         break
#     n = int(target[idx])
#     if button_tf[n]:  # 원하는 숫자가 있는 경우
#         number += target[idx]
#         if number == target:
#             if abs(100 - int(target)) < len(number):
#                 print(abs(100 - int(target)))
#             else:
#                 print(len(number))
#             break
#         idx += 1
#     else:  # 원하는 숫자가 없는 경우
#         level = 1
#         less = False
#         more = False
#         while (not less) and (not more):
#             if n - level < 0 and n + level > 9:  # 둘 다 인덱스를 벗어나면 멈추기
#                 break
#             if 0 <= n - level < 10 and button_tf[n - level]:  # 더 작은 숫자 중에서 있는 경우
#                 less = True
#                 num1 = number
#                 num1 += str(n - level)
#                 while len(num1) < len(target):  # 나머지는 가장 큰 숫자로 채워주어야 목표 채널에 가장 가까운 숫자를 만들 수 있음
#                     num1 += str(max_button)
#             if 0 <= n + level < 10 and button_tf[n + level]:  # 더 큰 숫자 중에서 있는 경우
#                 more = True
#                 num2 = number
#                 num2 += str(n + level)
#                 while len(num2) < len(target):  # 나머지는 가장 작은 숫자로 채워주어야 목표 채널에 가장 가까운 숫자를 만들 수 있음
#                     num2 += str(min_button)
#             else:
#                 level += 1
#         result = 500000
#         if less:
#             result = len(num1) + int(target) - int(num1)
#         if more:
#             temp = len(num2) + int(num2) - int(target)
#             if result > temp:
#                 result = temp
#         # 100에서 위 아래로 조종하는 것이 더 가까운 경우
#         if abs(100 - int(target)) < result:
#             result = abs(100 - int(target))
#         # 자릿수가 1자리 더 작은 경우
#         temp = str(max_button) * (len(target) - 1)
#         if len(temp) > 0 and len(temp) + abs(int(temp) - int(target)) < result:
#             result = len(temp) + abs(int(temp) - int(target))
#         # 자릿수가 1자리 더 큰 경우
#         if min_button != 0:
#             temp = str(min_button) * (len(target) + 1)
#             if len(temp) + abs(int(temp) - int(target)) < result:
#                 result = len(temp) + abs(int(temp) - int(target))
#         else:
#             n = 1
#             while n < 10 and not button_tf[n]:
#                 n += 1
#             if n != 10:
#                 temp = str(n) + "0" * len(target)
#                 if len(temp) + abs(int(temp) - int(target)) < result:
#                     result = len(temp) + abs(int(temp) - int(target))
#         print(result)
#         break