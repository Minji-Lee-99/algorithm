# 그룹 나누기
def union(x, y):
    global cnt
    while p[x] != x:
        x = p[x]
    while p[y] != y:
        y = p[y]
    if x == y:
        return
    p[y] = x
    cnt -= 1


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    p = [i for i in range(N + 1)]
    cnt = N
    for i in range(M):
        x, y = arr[2 * i], arr[2 * i + 1]
        union(x, y)
    print(f'#{tc} {cnt}')

