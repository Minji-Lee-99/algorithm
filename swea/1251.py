# 하나로
import heapq


def prim(s):
    # 힙에 시작점 넣어주기(힙은 환경부담금 기준 정렬)
    total = 0
    heap = []
    D[s] = 0
    heapq.heappush(heap, (D[s], s))
    while heap:
        # 최솟값 찾고, 방문 처리 해주기
        d, num = heapq.heappop(heap)
        if MST[num] == 1:  # 힙으로 하게 되면 갱신이 될 때마다 중복으로 들어가는 값들이 생김.
            continue
        MST[num] = 1
        total += d
        # 갱신해주기
        for i in range(N):
            if adjM[num][i] and MST[i] == 0:
                if D[i] > adjM[num][i]:
                    D[i] = adjM[num][i]
                    heapq.heappush(heap, (D[i], i))
    return total


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))
    e = float(input())
    adjM = [[0] * N for _ in range(N)]
    D = [2000000000001] * N
    MST = [0] * N
    # 각 해저터널별 환경부담금 계산
    for i in range(N):
        for j in range(i + 1, N):
            cost = (abs(x_list[i] - x_list[j])**2 + abs(y_list[i] - y_list[j])**2) * e
            adjM[i][j] = cost
            adjM[j][i] = cost
    print(f'#{tc} {round(prim(0))}')













