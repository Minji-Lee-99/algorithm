# 벽돌깨기
from copy import deepcopy
from collections import deque


def dfs(n, k, cnt, arr):
    global ans
    if cnt == 0:  # 남은 블록이 없다면 더 계산하는 것이 무의미하기 때문에 return
        ans = 0
        return
    if n == k:
        # 개수 cnt개수가 가장 작은 경우를 찾는 것이 목표!
        ans = min(ans, cnt)
        return
    else:
        for i in range(W):  # 공을 던질 열 선택하기
            if arr[H - 1][i] == 0:  # 공을 던질 필요가 없는 경우(제일 마지막 행이 0인 경우)
                continue
            for j in range(H):  # 공이 처음 맞는 위치 찾기
                if arr[j][i] != 0:
                    break
            cnt2 = cnt  # 현재 남아있는 블록의 개수 저장
            temp = deepcopy(arr)  # 현재의 블록 상태를 temp에 저장하고 temp를 조작
            q = deque([(j, i)])  # 제일 처음 구슬에 맞는 블록
            cnt2 -= 1  # 개수 계산
            temp[j][i] = 0
            # 벽돌 부수기
            while q:
                x, y = q.popleft()
                for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:  # 4방향 탐색
                    for level in range(1, arr[x][y]):  # 해당 위치에 적힌 숫자 많큼 depth들어가기
                        nx, ny = x + dx * level, y + dy * level
                        if 0 <= nx < H and 0 <= ny < W:  # 인덱스 벗어나는지 확인
                            if temp[nx][ny] > 1:  # 1보다 크다면 해당 위치를 기준으로 다시 4방향 탐색을 해야 하기 때문에 q에 넣어주기
                                temp[nx][ny] = 0  # 여러번 넣어지는 경우를 막기 위해서 0으로 만들기
                                cnt2 -= 1
                                q.append((nx, ny))
                            elif temp[nx][ny] == 1:  # 1인 경우는 그냥 해당 블록만 부서지기 때문에 부서진 개수 체크해주고, 0으로 만들기
                                temp[nx][ny] = 0
                                cnt2 -= 1
                        else:  # 인덱스 벗어나면 해당 방향은 더 볼 필요 없음
                            break
            # 블록 아래로 내리기
            for i in range(W):
                idx = H - 1  # 제일 마지막 위치 저장
                for j in range(H - 1, -1, -1):
                    if temp[j][i]:
                        temp[idx][i], temp[j][i] = temp[j][i], temp[idx][i]
                        idx -= 1
            dfs(n, k + 1, cnt2, temp)  # 다음 구슬의 위치 계산


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
    dfs(N, 0, cnt, arr)
    print(f'#{tc} {ans}')
