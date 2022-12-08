# 상근이의 여행
# 모든 정점이 연결되도록 스패닝 트리를 만드는 
T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    edge = []
    for i in range(M):
        edge.append(list(map(int, input().split())))
    print(N - 1)