# 세제곱근을 찾아라

import math
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    x = N ** (1.0/3.0)
    if abs(x - round(x, 1)) <= 1e-9:
        ans = int(round(x, 1))
    else:
        ans = -1
    print(f'#{tc} {ans}')
