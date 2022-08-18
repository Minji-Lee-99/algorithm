# 단지번호 붙이기
# dfs
def dfs(v):
    """
    시작점 v를 입력받아서 연결된 부분들을 탐색하고 개수를 리턴
    """
    cnt = 0
    stack = [v]
    while stack:
        n = stack.pop()
        if not visited[n[0]][n[1]]:
            visited[n[0]][n[1]] = True
            cnt += 1
            for dx, dy in [(1, 0), (0, 1), (0, -1), (-1, 0)]:
                nx = n[0] + dx
                ny = n[1] + dy
                if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and arr[nx][ny]:
                    stack.append((nx, ny))
    return cnt

N = int(input())
arr = [list(map(int, list(input()))) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
result = []
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            if arr[i][j] == 1:
                cnt = dfs((i, j))
                result.append(cnt)
            else:
                visited[i][j] = True
print(len(result))
result.sort()
for v in result:
    print(v)
