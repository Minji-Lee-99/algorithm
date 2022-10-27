# 활주로 건설
T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    # 가로 확인하기
    for i in range(N):
        num = []  # 예를 들어서  3 3 3 2 1 1로 지형이 주어졌다면 num = [3, 2, 1] cnt = [3, 1, 2]
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
            if -1 <= num[idx] - num[idx + 1] <= 1:  # 높이 차이가 1인 경우만 실행
                if num[idx] > num[idx + 1]:  # 경사로는 더 작은 쪽에 설치
                    if cnt[idx + 1] >= K:  # 경사로의 가로 길이보다 개수 더 많거나 같아야 설치 가능
                        cnt[idx + 1] -= K   # 이미 설치한 곳에는 또 설치가 불가능 하기 때문에 개수 빼주기
                    else:  # 설치할 공간이 없는 경우
                        break
                else:
                    if cnt[idx] >= K:
                        cnt[idx] -= K
                    else:  # 설치할 공간이 없는 경우
                        break
            else:  # 높이 차이가 1보다 크면 멈추기
                break
        else:  # break가 없는 경우에만 카운트
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
