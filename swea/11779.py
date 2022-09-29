# 그래프의 기본과 탐색: 연산
from collections import deque


def bfs():
    q = deque()
    q.append([N, 0])
    visited[N] = 1
    while q:
        n, cnt = q.popleft()
        if n == M:
            return cnt
        for i in [n + 1, n - 1, n * 2, n - 10]:
            if 0 < i <= 1000000 and visited[i] == 0:
                q.append([i, cnt + 1])
                visited[i] = 1


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    visited = [False] * 1000001
    print(f'#{tc} {bfs()}')

