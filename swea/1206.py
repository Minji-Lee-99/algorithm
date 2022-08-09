# 1206 View

import sys
sys.stdin = open("input.txt", "r")

for test_case in range(1, 11):
    N = int(input())
    h = list(map(int, input().split()))
    cnt = 0
    for i in range(2, N - 2):
        max_h = h[i - 2]
        for j in [-1, 1, 2]:
            if max_h < h[i + j]:
                max_h = h[i + j]
        if h[i] > max_h:
            cnt += (h[i] - max_h)
    print(f'#{test_case} {cnt}')