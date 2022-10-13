# 평범한 배낭
# 점화식: DP[i][w] = max(DP[i - 1][w], DP[i - 1][w - wi] + vi)
# i번째에서 최댓값은 i번째 물건을 선택하지 않고 i - 1번째 물건에서 w만큼의 무게가 있을 떄의 최댓값과
# i - 1번째에서 w - wi만큼의 무게 있을 때의 최대값에 현재 물건의 무게를 더한 무게 중 더 큰 값이다.
def knapsack():
    for i in range(1, N + 1):
        for w in range(1, K + 1):
            if W[i - 1] > w:
                DP[i][w] = DP[i - 1][w]
            else:
                DP[i][w] = max(DP[i - 1][w - W[i - 1]] + V[i - 1], DP[i - 1][w])
    return DP[N][K]


N, K = map(int, input().split())
DP = [[0] * (K + 1) for _ in range(N + 1)]
V = []
W = []
for _ in range(N):
    w, v = map(int, input().split())
    V.append(v)
    W.append(w)
print(knapsack())

# 1차원 리스트로 구현하기
def knapsack():
    for w, v in WV:
        for k in range(K, -1, -1):  # 0~K까지 순서대로 하게 되면 같은 item을 두번 선택하는 경우가 생긴다.
            if w > k:
                continue
            else:
                DP[k] = max(DP[k - w] + v, DP[k])
    return DP[K]


N, K = map(int, input().split())
DP = [0] * (K + 1)
WV = [list(map(int, input().split())) for _ in range(N)]
print(knapsack())

