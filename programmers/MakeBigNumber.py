def solution(number, k):
    Flag = True
    number = list(number)#문자열 형태를 리스트 형태로 변환
    i = 0
    count = 0
    while Flag:
        if count == k:#만약 제거한 숫자와 제거하려고 한 숫자의 개수가 같다면 함수 종료
            break
        if number[i] < number[i + 1]:#
            count+=1
            del number[i]
            i -= 1
            if i < 0:
                i = 0
        else:
            i += 1
        if i >= len(number)-1:
            for i in range(k-count):
                del number[-1]
            break
    return ''.join(number)

# print(solution("987654321", 2))
print(solution("1924", 4))
# print(solution("1231234", 3))
# print(solution("4177252841", 4))

# 첫번째 방법
# def solution(number, k):
#     for i in range(k):
#         max_num = number[1:]
#         for j in range(1, len(number)-1):
#             if number[0:j] + number[j + 1:] > max_num:
#                 max_num = number[0:j] + number[j + 1:]
#         if max_num < number[:-1]:
#             max_num =number[:-1]
#         number = max_num
#     return number
