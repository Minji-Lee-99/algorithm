# 보호필름
def bk(n, d, s): # 최대 깊이, 현재 깊이, 조합 시작 위치
    global flag, ans
    if flag:  # 답을 찾은 경우에는 재귀를 모두 빠져나가기
        return
    if n == d:  # 성능 검사
        for j in range(W):
            cnt = 1
            f = False  # 열 1개가 성능 통과했는지 판단하는 flag변수
            for i in range(D - 1):
                if arr[i][j] == arr[i + 1][j]:
                    cnt += 1
                else:
                    cnt = 1
                if cnt >= K:
                    break
            else:  # j번재 열이 통과X
                f = True
            if f:  # 1개라도 통과 못하면 탈락
                break
        else:  # 모두 통과한 경우에는 ans 갱신
            ans = n
            flag = True
        return
    else:
        for i in range(s, D - (n - d) + 1):
            a = arr[i][::]
            for j in range(W):  # i번째 줄 B로 변경
                arr[i][j] = 1
            bk(n, d + 1, i + 1)
            for j in range(W):  # i번째 줄 A로 변경
                arr[i][j] = 0
            bk(n, d + 1, i + 1)
            for j in range(W):  # i번째 줄 원상복귀
                arr[i][j] = a[j]


T = int(input())
for tc in range(1, T + 1):
    D, W, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(D)]
    ans = K  # 가능한 답의 최댓값은 K
    for i in range(K):  # 0 ~ K - 1까지 가능한 경우를 찾아보고 가능한 경우가 있으면 멈추기
        flag = False
        bk(i, 0, 0)
        if flag:  # 성능 통과한 경우
            break
    print(f'#{tc} {ans}')
