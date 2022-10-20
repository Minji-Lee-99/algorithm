# 원자 소멸 시뮬레이션
# 6천ms(정수) -> 1만3천(실수)
# 정수를 처리하는데 드는 비용보다 실수를 처리하는데 드는 비용이 압도적으로 많기 때문.
# 속도가 중요하다면 정수를 사용하는 것이 좋다.

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    now = [list(map(int, input().split())) for _ in range(N)]  # 구슬들의 현재 위치 담는 리스트
    cnts = {}  # 각 좌표에 몇개가 모였는지 체크
    next = []  # 구슬들의 다음 위치를 담는 리스트
    d = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    e = 0
    # 스케일 키우기( 정수로 계산하기 위해서)
    for p in now:
        p[0] = p[0] * 2 + 2000
        p[1] = p[1] * 2 + 2000
    while now:  # 구슬들이 없어질 때까지 진행
        for n in now:  # 현재 위치에서 각 구슬들을 진행방향으로 이동
            n[0] += d[n[2]][0]
            n[1] += d[n[2]][1]
            if 0 <= n[0] <= 4000 and 0 <= n[1] <= 4000:  # 이동한 곳이 범위 내라면 cnts개수 체크해준다. ( 범위 밖이라면 다른 구슬들과 부딪힐 일이 없으므로, next에 넣지 않음)
                if (n[0], n[1]) in cnts:
                    cnts[(n[0], n[1])] += 1
                else:
                    cnts[(n[0], n[1])] = 1
                next.append(n)
        now.clear()  # 초기화
        for p in next:  # next배열에 있는 구슬들을 꺼내서 여러 구슬이 같은 위치에 모인 경우(cnts로 판단)에는 구슬을 부수고 에너지를 더해줌
            if cnts[(p[0], p[1])] > 1:
                e += p[3]
            elif cnts[(p[0], p[1])] == 1:
                now.append(p)
        next.clear()  # 초기화
        cnts.clear()
    print(f'#{tc} {e}')




