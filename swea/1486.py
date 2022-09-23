# 장훈이의 높은 선반
T = int(input())
for tc in range(1, T + 1):
    n, h = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = 200000
    for i in range(1 << n):
        temp = 0
        for j in range(n):
            if i & (1 << j):
                temp += arr[j]
                if temp > ans:
                    break
        if h == temp:
            ans = temp
            break
        elif h < temp < ans:
            ans = temp
    print(f'#{tc} {ans - h}')
