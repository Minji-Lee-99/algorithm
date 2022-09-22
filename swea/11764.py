# 컨테이너 운반
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    w = list(map(int, input().split()))
    t = list(map(int, input().split()))
    w.sort(reverse=True)
    t.sort(reverse=True)
    total = j = 0
    for i in range(M):
        while j < N:
            if t[i] >= w[j]:
                total += w[j]
                j += 1
                break
            j += 1
    print(f'#{tc} {total}')
