# 벽돌깨기
from copy import deepcopy
from collections import deque


def dfs(n, k, cnt, arr):
    global ans
    if n == k:
        # 개수 cnt개수가 가장 작은 경우를 찾는 것이 목표!
        ans = max(ans, cnt)
    else:
        for i in range(W):  # 공을 던질 열 선택하기
            cnt2 = cnt
            if arr[i][H - 1] == 0:  # 공을 던질 필요가 없는 경우
                continue
            for j in range(H):
                if arr[i][j] != 0:
                    break
            temp = deepcopy(arr)
            q = deque([(i, j)])
            cnt2 -= 1
            while q:
                x, y = q.popleft()
                temp[x][y] = 0
                for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                    for level in range(arr[x][y]):
                        nx, ny = x + dx * level, y + dy * level
                        if 0 <= nx < H and 0 <= ny < W:
                            temp[nx][ny] = 0
                            if arr[nx][ny] > 1:
                                q.append((nx, ny))
                            elif arr[nx][ny] == 1:
                                cnt2 -= 1
                        else:
                            break
            dfs(n, k + 1, cnt2, temp)


T = int(input())
for tc in range(1, T + 1):
    N, W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]
    # 남은 벽돌의 개수 cnt에 저장해두기
    cnt = 0
    ans = 13 * 15
    for i in range(H):
        for j in range(W):
            if arr[i][j] != 0:
                cnt += 1

    # dfs돌리기


