import sys
from collections import deque
sys.setrecursionlimit(5000)


dx = [1, 0, 0, -1]
dy = [0, -1, 1, 0]
words = ['d', 'l', 'r', 'u']


"""
첫번째 풀이
DFS 사용
1~30은 통과
31은 시간초과
"""


def dfs(k, e, pos, word, n, m):
    if abs(pos[0] - e[0]) + abs(pos[1] - e[1]) > k:
        return ''
    if k == 0:
        return word
    for i in range(4):
        nx, ny = pos[0] + dx[i], pos[1] + dy[i]
        if 1 <= nx <= n and 1 <= ny <= m:
            result = dfs(k - 1, e, (nx, ny), word + words[i], n, m)
            if result != '':
                return result
    return ''


def solution(n, m, x, y, r, c, k):
    answer = dfs(k, (r, c), (x, y), '', n, m)
    if answer == '':
        answer = "impossible"
    return answer


print(solution(3, 4, 2, 3, 3, 1, 5))
print(solution(2, 2, 1, 1, 2, 2, 2))
print(solution(3, 3, 1, 2, 3, 3, 4))
print(solution(50, 50, 2, 2, 49, 49, 2500))
print(solution(6, 6, 2, 6, 6, 5, 11))
