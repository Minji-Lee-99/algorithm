# 줄기세포배양
# set은 탐색시간이 O(1) 해시 테이블
from queue import PriorityQueue


T = int(input())
for tc in range(1, T + 1):
    H, W, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]
    visited = set()
    inactive = PriorityQueue()
    active = PriorityQueue()
    sub = PriorityQueue()
    # 세포의 위치 추출
    for i in range(H):
        for j in range(W):
            if arr[i][j]:
                visited.add((i, j))
                inactive.put((arr[i][j], arr[i][j], i, j))
    del arr
    t = 1
    while t <= K:
        # sub에 있는거 배양해주기(4방향으로 탐색해서 inactive에 넣어주고, 원래 sub에 있는 포인트들은 active로 넣어주기)
        while sub.qsize():
            temp = sub.get()
            # 4방향 탐색
            for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                ni, nj = temp[2] + di, temp[3] + dj
                if not (ni, nj) in visited:
                    visited.add((ni, nj))
                    inactive.put((t + temp[1] * -1, temp[1] * -1, ni, nj))
            active.put(temp[0] + temp[1] * -1)
        # t초에 활성화 되는 세포들 옮기기
        while inactive.qsize():
            temp1 = inactive.get()
            if temp1[0] == t:  # 활성화 시키기
                sub.put((temp1[0], temp1[1] * -1, temp1[2], temp1[3]))
            else:
                inactive.put(temp1)
                break
        while active.qsize():
            temp2 = active.get()
            if temp2 != t:
                active.put(temp2)
                break
        t += 1
    print(f'#{tc} {active.qsize() + inactive.qsize()}')

    # del arr
    # t = 1
    # while t <= K:
    #     # sub에 있는거 배양해주기(4방향으로 탐색해서 inactive에 넣어주고, 원래 sub에 있는 포인트들은 active로 넣어주기)
    #
    #     # t초에 활성화 되는 세포들 옮기기
    #     while True:
    #         temp = inactive.get()
    #         if temp[0] == t:  # 활성화 시키기
    #             active.put(t + temp[1])
    #             visited.add((temp[2], temp[3]))
    #             if t + 1 <= K:
    #                 # 4방향 탐색
    #                 for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
    #                     ni, nj = temp[2] + di, temp[3] + dj
    #                     if not (ni, nj) in visited:
    #                         visited.add((ni, nj))
    #                         inactive.put((t + temp[1] + 1, temp[1], ni, nj))
    #         else:
    #             inactive.put(temp)
    #             break
    #     while active.qsize():
    #         temp2 = active.get()
    #         if temp2 != t:
    #             active.put(temp2)
    #             break
    #     t += 1
    # print(f'#{tc} {active.qsize() + inactive.qsize()}')







