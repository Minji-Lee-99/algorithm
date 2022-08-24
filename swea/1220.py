# Magnetic

# 1은 N 2는 S, 윗부분 N극, 아랫부분 S극
for tc in range(1, 11):
    N = int(input())
    tb = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for k in range(N):
        before = 0
        for l in range(N):
            if tb[l][k] == 1:
                before = 1
            if tb[l][k] == 2 and before == 1:
                cnt += 1
                before = 0
    print(f'#{tc} {cnt}')
