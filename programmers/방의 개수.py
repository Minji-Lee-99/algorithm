# 그래프
# 사이클이 몇개냐?
from collections import deque


# def find_set(v, p):
#     while v != p[v]:
#         v = p[v]
#     return p[v]


# def union(v1, v2, p):
#     p[find_set(v2)] = find_set(v1)


def dfs(adj):
    x, y = 0, 0
    for d in adj[(x, y)]:



def solution(arrows):
    answer = 0
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]
    adj = {(0, 0): set(), }
    p = {(0, 0): (0, 0)}
    x, y = 0, 0

    # 연결리스트 만들기(중복 제거)
    for d in arrows:
        nx, ny = x + dx[d], y + dy[d]
        if (nx, ny) in adj:
            adj[(nx, ny)].add((x, y))
        else:
            adj[(nx, ny)] = {(x, y)}
        adj[(x, y)].add((nx, ny))
        x, y = nx, ny
    print(adj)

    # 사이클 개수 찾기



print(solution([6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]))
print(solution([6, 5, 2, 7, 1, 4, 2, 4, 6]))
print(solution([5, 2, 7, 1, 6, 3]))
print(solution([6, 2, 4, 0, 5, 0, 6, 4, 2, 4, 2, 0]))