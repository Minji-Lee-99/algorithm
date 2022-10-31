# 무선 충전
def check():
    global total
    p1 = arr[x1][y1]
    p2 = arr[x2][y2]
    if not p1 and not p2:  # 둘다 충전할 수 있는 곳이 없는 경우
        return
    elif not p1:  # 둘 중 하나만 충전할 곳이 있는 경우
        total += p2[0][0]
    elif not p2:
        total += p1[0][0]
    else:  # 둘 다 1개 이상의 충전기가 있는 경우
        if p1[0] != p2[0]:
            total += p1[0][0]
            total += p2[0][0]
        else:
            total += p1[0][0]
            if len(p1) == 1 and len(p2) == 1:
                return
            elif len(p1) == 1:  # p1은 1개, p2는 2개 이상
                total += p2[1][0]
            elif len(p2) == 1:  # p1은 2개 이상, p2는 1개
                total += p1[1][0]
            else:  # 둘 다 2개 이상
                if p1[1][0] >= p2[1][0]:
                    total += p1[1][0]
                else:
                    total += p2[1][0]
    return


T = int(input())
for tc in range(1, T + 1):
    M, A = map(int, input().split())
    player1 = list(map(int, input().split()))
    player2 = list(map(int, input().split()))
    charge = [list(map(int, input().split())) for _ in range(A)]
    x1, y1, x2, y2 = 1, 1, 10, 10
    arr = [[[] for _ in range(11)] for _ in range(11)]
    di = [0, -1, 0, 1, 0]  # 상, 우, 하, 좌
    dj = [0, 0, 1, 0, -1]

    # 정렬해서 충전용량이 가장 큰 값이 먼저 저장되도록 하기
    charge.sort(key=lambda x: x[3], reverse=True)

    # 각 위치에 충전 가능한 충전기 번호 넣기
    for i in range(1, 11):
        for j in range(1, 11):
            for idx in range(A):
                c = charge[idx]
                if abs(i - c[1]) + abs(j - c[0]) <= c[2]:
                    arr[i][j].append((c[3], idx))

    # 시뮬레이션
    total = 0
    for i in range(M):
        check()
        x1, y1 = x1 + di[player1[i]], y1 + dj[player1[i]]
        x2, y2 = x2 + di[player2[i]], y2 + dj[player2[i]]
    check()
    print(f'#{tc} {total}')











