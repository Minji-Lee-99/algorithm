# 최소 신장 트리
# 1번 kruskal
# def find_set(x):
#     while x != p[x]:
#         x = p[x]
#     return p[x]
#
#
# def union(x, y):
#     p[find_set(y)] = find_set(x)
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     V, E = map(int, input().split())  # 정점의 마지막 번호, 간선 개수
#     edge = []
#     for _ in range(E):
#         s, e, w = map(int, input().split())
#         edge.append([w, s, e])
#     p = [i for i in range(V + 1)]
#     edge.sort()
#     ans = 0
#     cnt = 0
#     for w, s, e in edge:
#         if find_set(s) != find_set(e):
#             ans += w
#             cnt += 1
#             union(s, e)
#         if cnt == V:
#             break
#     print(f'#{tc} {ans}')


# prim
def prim():
    D[0] = 0
    total = 0
    for _ in range(V + 1):
        # 최솟값 찾기
        min_v = 100
        for i in range(V + 1):
            if MST[i] == 0 and min_v > D[i]:
                min_v = D[i]
                u = i
        MST[u] = 1  # 최솟값  MST에 추가해주기
        total += adjM[p[u]][u]
        # u와 연결되어 있는 값들 갱신해주기
        for i in range(V + 1):
            if MST[i] == 0 and adjM[u][i] and D[i] > adjM[u][i]:
                D[i] = adjM[u][i]
                p[i] = u
    return total


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    adjM = [[0] * (V + 1) for _ in range(V + 1)]
    MST = [0] * (V + 1)
    D = [100] * (V + 1)
    p = [i for i in range(V + 1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        adjM[s][e] = w
        adjM[e][s] = w
    print(f'#{tc} {prim()}')

