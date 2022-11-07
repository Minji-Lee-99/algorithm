# def solution(citations):
#     answer = 0
#     length = len(citations)
#     citations.sort(reverse=True)
#     if citations[length-1] >= length:
#         return length
#     for i in range(length):
#         if (citations[i] == i+1) and (length - (i+1)) <= (i+1):
#             answer = i+1
#             break
#         elif (citations[i] < i+1) and (length - (i+1)) <= (i+1):
#             max = citations[i]
#             # for j in range(citations[i]+1, citations[i-1]):
#             #     if i >= j and (length - i) <= j:
#             #         max = j
#             answer = max
#             break
#     return answer

# 주의할 부분! 꼭 리스트에 있는 값이 답인 것은 아니다. 예를 들어서 0, 1, 3, 7, 8, 9, 10, 11인 경우 5가 답이 된다.
# 또한 [10, 10, 10, 10, 10]인 경우 답이 5가 된다.
def solution(citations):
    answer = 0
    citations.sort()
    citations = [0] + citations  # [10, 10, 10, 10, 10]과 같은 경우를 해결하기 위해서
    answer = 0
    for i in range(len(citations)):
        if len(citations) - i >= citations[i]:
            answer = citations[i]
            if i == len(citations) - 1:  # 마지막 인덱스라면 중단
                return answer
            for j in range(citations[i] + 1, citations[i + 1]):  #[0, 1, 3, 7, 8, 9, 10, 11]인 경우를 위해서
                if len(citations) - i - 1 >= j:
                    answer = j
    return answer

