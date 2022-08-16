import sys
from collections import deque
sys.stdin = open("input_1227.txt", "r")


def bfs(miro):
    visited = []
    queue = deque([(1, 1)])
    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                nx = n[0] + dx
                ny = n[1] + dy
                if 0 <= nx < N and 0 <= ny < N:
                    if miro[nx][ny] == 3:
                        return 1
                    elif miro[nx][ny] == 0 and (nx, ny) not in visited:
                        queue.append((nx, ny))
    return 0


N = 100
for _ in range(10):
    tc = int(input())
    miro = [list(map(int, list(input()))) for _ in range(N)]
    print(f'#{tc} {bfs(miro)}')