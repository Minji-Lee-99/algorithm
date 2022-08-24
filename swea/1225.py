# 암호 생성기

from collections import deque

for _ in range(10):
    tc = int(input())
    queue = deque(map(int, input().split()))
    num = 0
    while 1:
        n = queue.popleft()
        n -= (num + 1)
        if n <= 0:
            queue.append(0)
            break
        else:
            queue.append(n)
            num = (num + 1) % 5
    print(f'#{tc}', end=' ')
    print(*queue)



