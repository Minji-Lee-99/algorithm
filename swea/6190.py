# 정곤이의 단조 증가하는 수

T = int(input())
for tc in range(1, 1 + T):
    N = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        for j in range(i, N):
            num = arr[i] * arr[j]
            flag = True
            rem1 = num % 20
            num = num // 10
            while num > 0:
                rem2 = num % 10
                if rem1 < rem2:
                    flag = False
                    break
                else:
                    rem1 = rem2
                num //= 10