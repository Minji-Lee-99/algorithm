from collections import deque
#	2, 10, [7, 4, 5, 6]
def solution(bridge_length, weight, truck_weights):
    #대기 트럭 리스트를 deque형식으로 바꿔준다.
    tw = deque(truck_weights)
    ing = deque()
    time = 0
    total = 0
    #시간 측정
    while True:
        time+=1
        for i in range(len(ing)):
            try:
                num = ing.popleft()
                if (time - num[1])%bridge_length == 0:
                    total -= num[0]
                else:
                    ing.appendleft(num)
                    break
            except:
                break
        if len(tw) >= 1:
            target = tw.popleft()
            if total + target <= weight:
                ing.append((target, time))
                total += target
            else: 
                tw.appendleft(target)
        if len(ing) < 1:
            break
    answer = time
    return answer
