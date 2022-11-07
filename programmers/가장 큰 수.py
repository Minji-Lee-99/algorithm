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
from functools import cmp_to_key


def mycmp(x, y):  # x가 더 큰 경우가 True, 반대가 False
    if len(x) == len(y):
        return x > y
    elif len(x) > len(y):
        temp = x[:len(y)]
        if temp == y:
            if x[len(y)] > '0':
                return True
            else:
                return False
        else:
            return temp > y
    else:  # y가 더 긴 경우
        temp = y[:len(x)]
        if temp == x:
            if y[len(x)] > '0':
                return False
            else:
                return True
        else:
            return x > temp


def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    print(numbers)
    numbers.sort(reverse=True)
    print(numbers)
    answer = ''.join(numbers)
    return answer




