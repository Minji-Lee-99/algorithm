# 보급로

from collections import deque


def BFS(v):
    q = deque([v])
    while q:
        i, j = q.popleft()
        for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N:
                # 시작점을 다시 보면 값이 이상해질 수 있으므로 시작점을 만나면 넘어가기
                if ni == 0 and nj == 0:
                    continue
                # 아직 방문 안한 정점이면 q에 넣어주고, 현재 위치에서 ni, nj위치의 시간 더해주기
                elif visited[ni][nj] == 0:
                    visited[ni][nj] = visited[i][j] + arr[ni][nj]
                    q.append((ni, nj))
                else:
                    # 이미 방문한 경우에는, 새로운 경로가 시간이 더 적게 든다면 갱신해주기, 그리고 값이 변경되면 다시 그 정점의 주변 정점을 갱신해주어야 하기 때문에 다시 q에 넣기
                    if visited[i][j] + arr[ni][nj] < visited[ni][nj]:
                        visited[ni][nj] = visited[i][j] + arr[ni][nj]
                        q.append((ni, nj))


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    visited[0][0] = 1
    BFS((0, 0))
    print(f'#{tc} {visited[N - 1][N - 1] - 1}')
