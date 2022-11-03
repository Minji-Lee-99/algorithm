# 무선 충전
def check():
    global total
    p1 = arr[x1][y1]  # 사람1의 현재 위치에서 충전할 수 있는 충전기 목록
    p2 = arr[x2][y2]  # 사람2의 현재 위치에서 충전할 수 있는 충전기 목록
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
    player1 = list(map(int, input().split()))  # 사람1의 이동
    player2 = list(map(int, input().split()))  # 사람2의 이동
    charge = [list(map(int, input().split())) for _ in range(A)]  # 충전기 정보
    x1, y1, x2, y2 = 1, 1, 10, 10
    arr = [[[] for _ in range(11)] for _ in range(11)]  # 각 좌표별로 충전가능한 충전기 정보 저장하는 리스트
    di = [0, -1, 0, 1, 0]  # 상, 우, 하, 좌
    dj = [0, 0, 1, 0, -1]

    # 정렬해서 충전용량이 가장 큰 값이 먼저 저장되도록 하기
    charge.sort(key=lambda x: x[3], reverse=True)

    # 각 위치에 충전 가능한 충전기 번호 넣기
    for i in range(1, 11):
        for j in range(1, 11):
            for idx in range(A):
                c = charge[idx]
                if abs(i - c[1]) + abs(j - c[0]) <= c[2]:  # i, j위치에서 각 충전기들까지 충전가능한 거리가 되는지 판단해보고, 되면 넣어주기
                    arr[i][j].append((c[3], idx))

    # 시뮬레이션
    total = 0
    for i in range(M):
        check()  # 현재 위치에서 충전이 가능하지 check
        x1, y1 = x1 + di[player1[i]], y1 + dj[player1[i]]  # 다음위치 갱신
        x2, y2 = x2 + di[player2[i]], y2 + dj[player2[i]]
    check()
    print(f'#{tc} {total}')











