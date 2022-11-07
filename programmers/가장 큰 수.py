# def comparison(a, b):
#     a = str(a)
#     b = str(b)
#     k = 0
#     while(True): # O(3)
#         try:
#             if a[k] < b[k]:
#                 return int(b)
#             elif a[k] > b[k]:
#                 return int(a)
#             else:
#                 k+=1
#         except:
#             len_a = len(a)
#             len_b = len(b)
#             if len_a > len_b:
#                 a_2 = a[len_b: len_a]
#                 if str(comparison(a_2, b)) == a_2:
#                     return int(a)
#                 else:
#                     return int(b)
#             elif len_a < len_b:
#                 b_2 = b[len_a: len_b]
#                 if str(comparison(a, b_2)) == b_2:
#                     return int(b)
#                 else:
#                     return int(a)
#             else:
#                 return int(a)
#
# def left(index):
#     return (index+index)+1
#
# def right(index):
#     return index*2+2
#
# def switch(ls, index1, index2):
#     ls[index1], ls[index2] = ls[index2], ls[index1]
#
# def heapify(ls, index):
#     l = left(index)
#     r = right(index)
#     while(l < len(ls)):
#         big = l
#         if r < len(ls) and comparison(ls[l], ls[r]) == ls[r]:
#             big = r
#         if comparison(ls[big], ls[index]) == ls[big]:
#             switch(ls, index, big)
#             index = big
#             l = left(index)
#             r = right(index)
#         else:
#             return
#     return ls
#
# def solution(numbers):
#     answer = ''
#     for i in range(len(numbers)//2, -1, -1):
#         heapify(numbers, i)
#     for i in range(len(numbers)):
#         switch(numbers, 0, len(numbers)-1)
#         m = numbers.pop()
#         answer += str(m)
#         heapify(numbers, 0)
#     return str(int(answer))









#################################################################################
# 정렬하되, 가장 높은 자릿수의 숫자가 큰 순서대로 정렬하며, 6, 60의 경우 6이 더 큼
# def mycmp(x, y):  # x가 더 큰 경우가 True, 반대가 False
#     if x == y:
#         return 0
#     elif len(x) == len(y):
#         if x > y:
#             return 1
#         else:
#             return -1
#     elif len(x) > len(y):
#         temp = x[:len(y)]
#         if temp == y:
#             if x[len(y)] > '0':
#                 return 1
#             else:
#                 return -1
#         else:
#             if temp> y:
#                 return 1
#             else:
#                 return -1
#     else:  # y가 더 긴 경우
#         temp = y[:len(x)]
#         if temp == x:
#             if y[len(x)] > '0':
#                 return -1
#             else:
#                 return 1
#         else:
#             if x > temp:
#                 return 1
#             else:
#                 return -1

from functools import cmp_to_key


def mycmp(x, y):  # x가 크면 양수, y가 크면 음수, 같으면 0
    temp1 = x + y   # 두 숫자를 순서를 달리하여 이어 붙였을 때, 먼저 붙인 숫자가 더 큰 경우 해당 숫자가 더 우선순위가 높은 것
    temp2 = y + x
    if temp1 == temp2:
        return 0
    elif temp1 > temp2:
        return 1
    else:
        return -1


def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    numbers.sort(key=cmp_to_key(mycmp), reverse=True)  # 위에서 정의한 mycmp로 정렬
    answer = str(int(''.join(numbers)))  # 0만 들어오는 경우 답은 000이 아니라 0이어야 한다.
    return answer
