# 고대 유적

T = int(input())
for tc in range(1, 1 + T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    ans = 0
    # 가로로 확인하는 경우
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                cnt += 1
            else:
                if cnt > ans:
                    ans = cnt
                cnt = 0
        if cnt > ans:
            ans = cnt
        cnt = 0

    # 세로로 확인하는 경우
    for j in range(M):
        for i in range(N):
            if arr[i][j] == 1:
                cnt += 1
            else:
                if cnt > ans:
                    ans = cnt
                cnt = 0
        if cnt > ans:
            ans = cnt
        cnt = 0
    print(f'#{tc} {ans}')
