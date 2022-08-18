# 길찾기
# S: 0, G: 99 -> SG사이 경로가 존재하는가?
# 나는 보는 와중에 체크 했으나, 그냥 순회하고 목표지점의 visited 결과를 보면 됨
import sys
sys.stdin = open("input_1219.txt", "r")


# def dfs(v):
#     stack = []
#     visited[v] = True
#     flag = 0
#     while 1:
#         for w in adj[v]:
#             if not visited[w]:
#                 stack.append(v) # 현재 상태에서 더 들어갈 곳이 있으면 더 들어가기 위해서 돌아올 곳을 지정
#                 v = w
#                 visited[w] = True
#                 if v == G:
#                     flag = 1
#                     return flag
#                 break
#         else:
#             if stack:
#                 v = stack.pop()
#             else:
#                 break
#     return flag


def dfs(v):
    global flag
    visited[v] = True
    if v == G:
        flag = 1
    for w in adj[v]:
        if not visited[w]:
            dfs(w)
    return


for _ in range(10):
    tc, E = map(int, input().split())
    temp = list(map(int, input().split()))
    adj = [[] for _ in range(101)]
    visited = [False] * 101
    S = 0
    G = 99
    for i in range(E):
        a, b = temp[2 * i], temp[2 * i + 1]
        adj[a].append(b)
    flag = 0
    dfs(S)
    print(f'#{tc} {flag}')
