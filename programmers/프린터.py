from collections import deque

def solution(priorities, location):
    sorted_list = deque()
    #순서대로 정렬하고 우리가 알고자 하는 입력의 위치를 알기 위해서 위치 정보를 담은 pair형식으로 바꿔준다. 
    for i in range(len(priorities)):
        priorities[i] = (priorities[i], i)
    for j in range(0, len(priorities)):
        max = 0
        for i in range(1, len(priorities)):
            if priorities[i][0] > priorities[max][0]:
                max = i
        num = priorities.pop(max)
        sorted_list.append(num)
        priorities = priorities[max:len(priorities)] + priorities[0:max]
    for i in range(len(sorted_list)):
        if sorted_list[i][1] == location:
            answer = i+1
            break
    return answer
