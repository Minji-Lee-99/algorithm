# 오목 판정
def check():
    for i in range(N):
        for j in range(N):
            if i > (N - 4) and j > (N - 4):
                continue
            if arr[i][j] == 'o':
                for di, dj in [[0, 1], [1, 1], [1, 0], [1, -1]]:
                    cnt = 1
                    for k in range(1, 5):
                        ni, nj = i + di * k, j + dj * k
                        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 'o':
                            cnt += 1
                        else:
                            break
                    if cnt == 5:
                        return 'YES'
    return 'NO'


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    print(f'#{tc} {check()}')

