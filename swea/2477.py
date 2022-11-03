# 차량 정비소
from heapq import heappush, heappop
from collections import deque

T = int(input())
for tc in range(1, T + 1):
    N, M, K, A, B = map(int, input().split()) # 접수창구 개수, 정비창구 개수, 고객수, 지갑을 두고 간 고객이 이용한 접수창구 번호, 정비창구 번호
    A_time = [0] + list(map(int, input().split()))
    B_time = [0] + list(map(int, input().split()))
    customer_time = [0] + list(map(int, input().split()))

    receipt = [[-1, -1] for _ in range(N + 1)]  # 접수 창구
    wait_receipt = deque()  # 대기자 번호, 일반 큐 (고객 번호가 작은 순인데, 시간 순서대로 들어오기 때문에 따로 정렬해줄 필요가 없음)
    left_receipt = [i for i in range(1, N + 1)]  # 빈 접수 창구 번호 저장, 우선순위 큐(오름차순) (창구 번호가 작은 곳이 우선순위)
    repair = [[-1, -1] for _ in range(M + 1)]  # 정비 창구
    wait_repair = deque()  # 대기하는 사람 번호, 일반 큐 ( 대기 순서대로 이기 떄문에)
    left_repair = [i for i in range(1, M + 1)]  # 빈 정비 창구 번호 저장, 우선순위 큐(오름차순) (창구 번호가 작은 곳이 우선순위)

    result = [[0, 0] for i in range(K + 1)]  # 고객이 이용한 접수 창구 번호, 정비창구 번호 저장

    t = customer_time[1]
    max_t = 40 * K  # 모든 사람이 가장 오래 걸린 경우 계산
    idx = 1  # 손님 현재 번호
    while t <= max_t:
        # t시간에 도착한 사람들 접수 대기자 명단으로 옮기기
        while idx <= K:
            if customer_time[idx] == t:
                wait_receipt.append(idx)
                idx += 1
            else:
                break
        # 접수 창구에서 t초에 끝난 사람들이 있으면 정비 창구 대기열로 옮기기
        for i in range(1, N + 1):
            if receipt[i][1] == t:
                wait_repair.append(receipt[i][0])  # 고객 번호를 정비 대기열로 보내기
                receipt[i] = [-1, -1]  # 해당 접수 창구 비우기
                heappush(left_receipt, i)  # 빈 접수창구 리스트에 접수창구 번호 넣어주기
        # 접수 창구 대기자 명단에 있는 사람들 접수 창구에 빈자리 있으면 옮기기
        while left_receipt and wait_receipt:
            r = heappop(left_receipt)  # 창구 번호
            c = wait_receipt.popleft()  # 손님 번호
            receipt[r] = [c, t + A_time[r]]  # 손님 번호, 접수 끝나는 시간
            result[c][0] = r  # c번 손님이 어디에서 접수했는지 저장해주기
        # 정비 창구에서 t초에 수리가 완료된 사람 내보내기
        for i in range(1, M + 1):
            if repair[i][1] == t:
                repair[i] = [-1, -1]  # 정비 창구 비우기
                heappush(left_repair, i)  # 빈 정비 창구 리스트에 창구 번호 넣어주기
        # 정비 대기 창구에 있는 사람들 정비 창구로 옮기기
        while left_repair and wait_repair:
            r = heappop(left_repair)  # 창구 번호
            c = wait_repair.popleft()  # 손님 번호
            repair[r] = [c, t + B_time[r]]  # 정비 창구에 넣어주기
            result[c][1] = r  # c번 손님이 어디에서 정비했는지 번호 넣어주기
        t += 1  # 시간 갱신

    # A에서 접수하고 B에서 수리한 사람이 있는지 확인하고 있다면 번호 더해주기
    ans = 0
    for i in range(1, K + 1):
        if result[i] == [A, B]:
            ans += i

    # 0이면 A에서 접수하고 B에서 수리한 사람이 없다는 뜻이므로 -1출력
    if ans == 0:
        ans = -1

    # 결과 출력
    print(f'#{tc} {ans}')












