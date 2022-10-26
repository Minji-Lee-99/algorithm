# 활주로 건설
T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    # 가로 확인하기
    for i in range(N):
        num = []
        cnt = []
        now = arr[i][0]
        c = 0
        for j in range(N):
            if now == arr[i][j]:
                c += 1
            else:
                num.append(now)
                cnt.append(c)
                c = 1
                now = arr[i][j]
        num.append(now)
        cnt.append(c)
        for idx in range(len(num) - 1):
            if -1 <= num[idx] - num[idx + 1] <= 1:
                if num[idx] > num[idx + 1]:
                    if cnt[idx + 1] >= K:
                        cnt[idx + 1] -= K
                    else:
                        break
                else:
                    if cnt[idx] >= K:
                        cnt[idx] -= K
                    else:
                        break
            else:
                break
        else:
            ans += 1

    # 세로 확인하기
    for j in range(N):
        num = []
        cnt = []
        now = arr[0][j]
        c = 0
        for i in range(N):
            if now == arr[i][j]:
                c += 1
            else:
                num.append(now)
                cnt.append(c)
                c = 1
                now = arr[i][j]
        num.append(now)
        cnt.append(c)
        for idx in range(len(num) - 1):
            if -1 <= num[idx] - num[idx + 1] <= 1:
                if num[idx] > num[idx + 1]:
                    if cnt[idx + 1] >= K:
                        cnt[idx + 1] -= K
                    else:
                        break
                else:
                    if cnt[idx] >= K:
                        cnt[idx] -= K
                    else:
                        break
            else:
                break
        else:
            ans += 1
    print(f'#{tc} {ans}')
