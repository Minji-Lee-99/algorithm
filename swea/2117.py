# 홈 방범 서비스

def solve():
    ans = 0
    # (x, y)좌표를 기준으로 k = N + 1 -> 1로 감소시킴
    for k in range(N + 1, 0, -1): # k값 정해주기(마름모의 지름)
        for x in range(N): # 마름모 중심의 위치 잡아주기
            for y in range(N):
                cnt = 0
                for hx, hy in home: # 집들의 위치를 다 가지고 와서 마름모 중심까지의 거리 계산하기
                    if abs(x - hx) + abs(y - hy) < k:
                        cnt += 1
                if M * cnt - cost[k] >= 0 and ans < cnt: # 손해를 보지 않고, 저장된 값보다 집의 숫자가 더 많다면 갱신해주기
                    ans = cnt
    return ans


# k에 따른 비용을 미리 계산
cost = [0] * 22
cost[1] = 1
for k in range(2, 22):
    cost[k] = k * k + (k - 1) * (k - 1)
T = int(input())
for tc in range(1, T + 1):
    # 도시의 크기와 집당 지불하는 비용
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 집의 좌표 저장
    home = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                home.append((i, j))
    print(f'#{tc} {solve()}')



# 인터넷 찾아서 푼 풀이
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    house = []
    ans = 0
    # house에 집의 좌표 넣기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                house.append([i, j])
    # 마름모의 지름을 구하고, 마름모의 중심 좌표를 배열에서 하나씩 이동하면서, 모든 집들의 마름모 중심까지의 거리를 구해서 마름모 안에 들어오는지 판단
    for k in range(1, N + 3):
        for i in range(N):
            for j in range(N):
                cnt = 0
                for x, y in house:
                    if abs(i-x) + abs(j-y) < k:
                        cnt += 1
                if k * k + (k-1) * (k-1) <= cnt * M and cnt > ans:
                    ans = cnt
    print(f'#{tc} {ans}')

