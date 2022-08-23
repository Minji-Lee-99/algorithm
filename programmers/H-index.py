def solution(citations):
    answer = 0
    length = len(citations)
    citations.sort(reverse=True)
    if citations[length-1] >= length:
        return length
    for i in range(length):
        if (citations[i] == i+1) and (length - (i+1)) <= (i+1):
            answer = i+1
            break
        elif (citations[i] < i+1) and (length - (i+1)) <= (i+1):
            max = citations[i]
            # for j in range(citations[i]+1, citations[i-1]):
            #     if i >= j and (length - i) <= j:
            #         max = j
            answer = max
            break
    return answer
