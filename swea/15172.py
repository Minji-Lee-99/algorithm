# 헌터
def candidate(k, n):
    candi = []
    for i in range(k, n):
        if visit_order[i] > 0:
            candi.append(i)
        else:
            flag = False
            for j in range(0, k):
                if visit_order[j] * -1 == visit_order[i]:
                    flag = True
            if flag:
                candi.append(i)
    return candi


def perm(k, n, location, total):
    global ans
    if ans < total:
        return
    if k == n:
        if ans > total:
            ans = total
        return
    else:
        candi = candidate(k, n)
        for i in candi:
            visit_order[k], visit_order[i] = visit_order[i], visit_order[k]
            perm(k + 1, n, pos[visit_order[k]], total + abs(location[0] - pos[visit_order[k]][0]) + abs(location[1] - pos[visit_order[k]][1]))
            visit_order[k], visit_order[i] = visit_order[i], visit_order[k]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visit_order = []
    pos = {}
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                pos[arr[i][j]] = (i, j)
                visit_order.append(arr[i][j])
    ans = N * 2 * 8
    perm(0, len(visit_order), (0, 0), 0)
    print(f'#{tc} {ans}')
