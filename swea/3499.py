# 퍼펙트 셔플

import math

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    deck = input().split()
    mid = math.ceil(N / 2)
    result = [0] * N
    i = k = 0
    j = mid
    while i < mid or j < N:
        if i < mid:
            result[k] = deck[i]
            i += 1
            k += 1
        if j < N:
            result[k] = deck[j]
            j += 1
            k += 1
    print(f'#{tc}', end=' ')
    print(*result)
