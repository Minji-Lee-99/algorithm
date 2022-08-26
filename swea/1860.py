# 진기의 최고급 붕어빵

T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    sec = list(map(int, input().split()))
    cnt = 0
    sec.sort()
    flag = True
    for s in sec:
        if s // M * K - cnt > 0:
            cnt += 1
        else:
            flag = False
            break
    if flag:
        print(f'#{tc} Possible')
    else:
        print(f'#{tc} Impossible')
