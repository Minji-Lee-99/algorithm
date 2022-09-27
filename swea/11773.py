# 전기버스2 - 백트래킹
def bt(n, k, cnt, power): # n은 충전기 개수, k는 위치, cnt는 충전한 개수, power은 현재 갈 수 있는 거리
    global ans
    if ans < cnt:
        return
    if k == n or power >= n - k:
        ans = min(ans, cnt)
        return
    else:
        bt(n, k + 1, cnt + 1, arr[k] - 1)  # k번째 충전기에서 충전한 경우
        if power > 0:  # 현재 남은 power가 있어야 충전 안하고 갈 수 있음
            bt(n, k + 1, cnt, power - 1)  # k번째 충전기에서 충전 안한 경우


T = int(input())
for tc in range(1, T + 1):
    arr = list(map(int, input().split()))
    N = arr[0]
    arr = arr[1:]
    ans = 100
    bt(N - 1, 1, 0, arr[0] - 1)
    print(f'#{tc} {ans}')


