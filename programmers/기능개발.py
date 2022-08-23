from collections import deque
import math

def solution(progresses, speeds):
    answer = []
    time = 0
    progresses = deque(progresses)
    speeds = deque(speeds)
    while True:
        if len(progresses) < 1:
            break
        p = progresses.popleft()
        s = speeds.popleft()
        count = 1
        p += s*time
        time = time + math.ceil((100-p)/s)
        while True:
            if len(progresses) < 1:
                break
            p1 = progresses.popleft()
            s1 = speeds.popleft()
            if p1 + time*s1 >= 100:
                count +=1
            else:
                progresses.appendleft(p1)
                speeds.appendleft(s1)
                break
        answer.append(count)
    return answer
