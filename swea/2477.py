# 차량 정비소
from heapq import heappush, heappop
from collections import deque

T = int(input())
for tc in range(1, T + 1):
    N, M, K, A, B = map(int, input().split()) # 접수창구 개수, 정비창구 개수, 고객수, 지갑을 두고 간 고객이 이용한 접수창구 번호, 정비창구 번호
    A_time = [0] + list(map(int, input().split()))
    B_time = [0] + list(map(int, input().split()))
    customer_time = [0] + list(map(int, input().split()))

    receipt = [[] for _ in range(N + 1)]
    wait_receipt = []  # 대기자 번호, 일반 큐
    left_receipt = [i for i in range(1, N + 1)]  # 빈 접수 창구 번호 저장, 우선순위 큐(오름차순)
    repair = [[] for _ in range(M + 1)]
    wait_repair = []  # 대기하는 사람 번호, 일반 큐
    left_repair = [i for i in range(1, M + 1)]  # 빈 정비 창구 번호 저장, 우선순위 큐(오름차순)

    result = [[] for i in range(K + 1)]  # 고객이 이용한 접수 창구 번호, 정비창구 번호 저장

    t = customer_time[1]
    idx = 1  # 손님 현재 번호
    while True:
        # t시간에 도착한 사람들 접수 대기자 명단으로 옮기기
        while idx <= K:
            if customer_time[idx] == t:
                wait_receipt.append


