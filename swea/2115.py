# 벌꿀채취
# 두명이 길이 M의 꿀통을 고르는 조합
def comb(n, k, s, ssum):
    global ans
    if n == k:  # 두명 모두 골랐을 때, 최댓값 갱신
        ans = max(ans, ssum)
        return
    idx = s  # 이전에 선택한 곳 이후부터 시작
    while idx < N ** 2:
        i, j = idx // N, idx % N  # idx에서 i, j 계산
        if j > N - M:  # 인덱스를 벗어나는 경우
            idx += 1
            continue
        if j <= (N - M ** 2):  # 현재 선택한 꿀통과 겹치지 않으면서, 선택할 수 있는 길이 M의 꿀통이 있는지
            comb(n, k + 1, i * N + j + M, ssum + memo[i][j])
        else:  # 없으면 행 바꾸기
            comb(n, k + 1, (i + 1) * N, ssum + memo[i][j])
        idx += 1
    return


# 길이 M의 꿀통을 선택했을 때, 그 안에서 최댓값을 구하는 함수
def powerset(n, k, ssum, ssum2, rs):
    global price
    if ssum > C:  # 현재까지 선택한 꿀통의 무게가 딸 수 있는 꿀통의 무게를 넘은 경우
        return
    if rs ** 2 + ssum2 <= price:  # 현재까지 선택한 꿀통과 남은 꿀통을 모두 딴다고 해도 현재 최댓값 보다 작거나 같은 경우
        return
    if n == k:  # 끝까지 도달한 경우
        price = max(price, ssum2)
        return
    powerset(n, k + 1, ssum + temp[k], ssum2 + temp[k] ** 2, rs - temp[k])  # k번째 인덱스 선택한 경우
    powerset(n, k + 1, ssum, ssum2, rs - temp[k])  # k번째 인덱스 선택하지 않은 경우


T = int(input())
for tc in range(1, T + 1):
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    memo = [[0] * (N - M + 1) for _ in range(N)]
    ans = 0

    # 특정 위치를 선택했을 때, 가질 수 있는 최대 가격을 미리 계산해두기
    for i in range(N):
        for j in range(N - M + 1):
            temp = arr[i][j: j + M]
            price = 0
            powerset(M, 0, 0, 0, sum(temp))
            memo[i][j] = price

    # memo에서 조합으로 2개를 선택한 것중 가장 값이 큰 경우 찾기
    comb(2, 0, 0, 0)
    print(f'#{tc} {ans}')

