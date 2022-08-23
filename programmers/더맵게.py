import heapq

def solution(scoville, K):
    #scoville 리스트를 힙으로 변환
    heapq.heapify(scoville)
    answer = 0
    while (True):
        try:
            m1 = heapq.heappop(scoville)
            if m1 < K:
                m2 = heapq.heappop(scoville)
                m3 = m1 + 2*m2
                heapq.heappush(scoville, m3)
                answer += 1
            else:
                break
        except:
            answer = -1
            break
    return answer
