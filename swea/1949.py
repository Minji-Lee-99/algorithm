# 등산로 조성
def dfs(s, cut, length):
    global ans
    if length > ans:  # ans보다 현재 길이가 더 길면 갱신
        ans = length
    x, y = s
    for dx, dy in [[0, 1], [1, 0], [-1, 0], [0, -1]]:  # 4방향으로 갈 수 있는 곳 체크
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:  # index를 벗어나지 않았고, 방문을 안한 곳
            if arr[nx][ny] < arr[x][y]:  # 높이가 낮아지는 곳이면 방문
                visited[nx][ny] = 1
                dfs((nx, ny), cut, length + 1)
                visited[nx][ny] = 0
            elif cut == 0 and arr[nx][ny] - arr[x][y] + 1 <= K:  # 높이가 높거나 같은 곳인데, 아직 산을 갂을 수 있는 기회가 남아있고, 현재 위치보다 1적게 갂을 수 있는 곳인지 확ㅇ인
                temp = arr[nx][ny]  # 원래 값 저장
                arr[nx][ny] = arr[x][y] - 1  # 갂는 경우 현재 위치보다 딱 1작게 갂는 것이 가장 긴 등산로를 찾을 수 있는 경우임
                visited[nx][ny] = 1
                dfs((nx, ny), 1, length + 1)
                arr[nx][ny] = temp  # 변경한 값 복구
                visited[nx][ny] = 0


T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_v = arr[0][0]
    max_l = []
    ans = 0
    # 최댓값(시작점) 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j] > max_v:  # max_v보다 더 큰 값이 있다면 갱신
                max_v = arr[i][j]
                max_l = [(i, j)]
            elif arr[i][j] == max_v:  # max_v와 같은 값이 있다면 리스트에 저장
                max_l.append((i, j))
    for s in max_l:  # 각 시작점을 하나씩 가지고 와서 dfs돌리기
        visited = [[0] * N for _ in range(N)]  # 방문처리를 위한 리스트를 만들어주고, 시작점은 방문처리
        visited[s[0]][s[1]] = 1
        dfs(s, 0, 1)
    print(f'#{tc} {ans}')
