# 탈주범 검거
from collections import deque


def bfs(s):
    q = deque([s])
    visited[s[0]][s[1]] = 1
    cnt = 1
    while q:
        i, j = q.popleft()
        if visited[i][j] == L:  # 해당 위치에 도달했을 때의 시간이 주어진 시간과 같다면 다음 위치를 볼 필요가 없음
            continue
        for d in shape[arr[i][j]]:  # 해당 파이프를 통해서 갈 수 있는 방향
            ni, nj = i + di[d], j + dj[d]
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and possible_pipe[d][arr[ni][nj]]:  # 해당 위치가 방문하지 않았고, 갈 수 있는 길인 경우
                visited[ni][nj] = visited[i][j] + 1  # 시간 체크
                cnt += 1  # 개수 체크
                if visited[ni][nj] < L:  # 현재 시간이 주어진 시간보다 작은 경우에만 q에 추가. 주어진 시간이 3인데 현재 위치 도달 시간이 3이면 다음걸 볼 필요 X
                    q.append((ni, nj))
    return cnt


T = int(input())
for tc in range(1, T + 1):
    N, M, X, Y, L = map(int, input().split())  # 행의 길이, 열의 길이, 맨홀의 x, y좌표, 시간
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    di = [-1, 0, 0, 1]
    dj = [0, -1, 1, 0]
    shape = [[], [0, 1, 2, 3], [0, 3], [1, 2], [0, 2], [2, 3], [1, 3], [1, 0]]  # 해당 파이프를 통해서 갈 수 있는 방향 -> 1번 파이프는 상하좌우 다 갈 수 있음
    possible_pipe = [[0, 1, 1, 0, 0, 1, 1, 0], [0, 1, 0, 1, 1, 1, 0, 0], [0, 1, 0, 1, 0, 0, 1, 1], [0, 1, 1, 0, 1, 0, 0, 1]]  # 각 방향별로 연결될 수 있는 파이프의 번호
    print(f'#{tc} {bfs((X, Y))}')
