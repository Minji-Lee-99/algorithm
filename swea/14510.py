T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    arr2 = []
    n = max(arr)
    day = 0
    for i in range(N):
        m = n - arr[i]
        day += (m // 3) * 2
        if m % 3:
            arr2.append(m % 3)
    c1 = arr2.count(1)
    c2 = arr2.count(2)
    if c1 == c2:
        day += c1 * 2
    elif c1 < c2:
        c2 -= c1
        day += c1 * 2
        if c2 > 0:
            day += (c2 // 3)
            c2 = c2 % 3
            day += c2 * 2
    else:
        c1 -= c2
        day += c2 * 2
        day += 1
        c1 -= 1
        if c1 > 0:
            day += c1 * 2
    print(f'#{tc} {day}')


