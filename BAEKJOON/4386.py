# 별자리 만들기
# 전형적인 MST문제
# 크루스칼 알고리즘 사용

# 부모 찾기
def find_parent(x):
    while x != parent[x]:
        x = parent[x]
    return x

# x, y를 같은 영역으로 합치기
def union(x, y):
    parent[find_parent(y)] = parent[find_parent(x)]


N = int(input())
pos = [[], ]
edge = []
for i in range(N):
    pos.append(list(map(float, input().split())))
# 각 정점별로 weight값 계산하기
for i in range(1, N + 1):
    for j in range(i + 1, N + 1):
        dis = ((pos[i][0] - pos[j][0]) ** 2 + (pos[i][1] - pos[j][1]) ** 2) ** (1/2)
        edge.append([dis, i, j])
edge.sort()  # 정점을 weight기준으로 정렬하기
parent = [i for i in range(N + 1)]  # 대표자
result = 0
cnt = 0
for e in edge:
    if find_parent(e[1]) != find_parent(e[2]):  # 정점에 circle이 생기지 않는 경우에만 선택
        union(e[1], e[2])  # 합쳐주기
        result += e[0]
        cnt += 1
    if cnt == N - 1:  # N - 1개를 선택하면, MST가 완성된 것이므로 멈추기
        print(round(result, 2))
        break



