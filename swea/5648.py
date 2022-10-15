# 원자 소멸 시뮬레이션
# 정수를 처리하는데 드는 비용보다 실수를 처리하는데 드는 비용이 압도적으로 많기 때문.
# 속도가 중요하다면 정수를 사용하는 것이 좋다.
# 6천ms(정수) -> 1만3천(실수)
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    now = [list(map(int, input().split())) for _ in range(N)]
    cnts = {}
    next = []
    d = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    e = 0
    # 스케일 키우기
    for p in now:
        p[0] = p[0] * 2 + 2000
        p[1] = p[1] * 2 + 2000
    while now:
        for n in now:
            n[0] += d[n[2]][0]
            n[1] += d[n[2]][1]
            if 0 <= n[0] <= 4000 and 0 <= n[1] <= 4000:
                if (n[0], n[1]) in cnts:
                    cnts[(n[0], n[1])] += 1
                else:
                    cnts[(n[0], n[1])] = 1
                next.append(n)
        now.clear()
        for p in next:
            if cnts[(p[0], p[1])] > 1:
                e += p[3]
            elif cnts[(p[0], p[1])] == 1:
                now.append(p)
        next.clear()
        cnts.clear()
    print(f'#{tc} {e}')




