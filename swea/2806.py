# N-Queen
#백트래킹

def bt(k):
    global cnt
    if k == N:
        cnt += 1
        return
    else:
        for j in range(N):  # 기본 후보는 k행의 모든 컬럼
            flag = True
            for i in range(k):
                # 대각선에 퀸이 위치하고 있거나, 같은 컬럼 상에 퀸이 위치한 경우
                if abs(i - k) == abs(col[i] - j) or col[i] == j:
                    flag = False
                    break
            if flag:    # 해당 컬럼이 다른 퀸에게 공격당하지 않는 경우에만 다음 행으로 넘어감
                col[k] = j  # 어차피 다시 갱신될 부분이고 다시 볼때도 k - 1까지만 볼거라 초기화 불필요
                bt(k + 1)   # 그 다음 행에 퀸 위치 탐색
    return


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    col = [0] * N
    cnt = 0
    bt(0)
    print(f'#{tc} {cnt}')
